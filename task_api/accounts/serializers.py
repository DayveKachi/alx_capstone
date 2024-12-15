from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ("id", "email", "username", "password", "confirm_password")
        read_only_fields = ("id",)

    def validate(self, attrs):
        if self.context["request"].method == "POST":
            password = attrs.get("password")
            confirm_password = attrs.get("confirm_password")
            if not password or not confirm_password:
                raise serializers.ValidationError("Both password fields are required.")
            if password != confirm_password:
                raise serializers.ValidationError("Both password fields must match.")
        elif "password" in attrs or "confirm_password" in attrs:
            if attrs.get("password") != attrs.get("confirm_password"):
                raise serializers.ValidationError("Both password fields must match.")
        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password", None)
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        validated_data.pop("confirm_password", None)
        if password:
            instance.password = make_password(password)
        return super().update(instance, validated_data)
