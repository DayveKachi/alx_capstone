from rest_framework import serializers
from .models import Task
from django.utils import timezone


class TaskSerializer(serializers.ModelSerializer):
    """Serialize data for the Task model"""

    class Meta:
        model = Task
        fields = (
            "title",
            "owner",
            "description",
            "due_date",
            "priority_level",
            "status",
            "completed_timestamp",
        )
        read_only_fields = ("owner", "completed_timestamp", "status")

    def validate(self, attrs):
        due_date = attrs.get("due_date")
        priority = attrs.get("priority_level")
        if due_date > timezone.now().date():
            raise serializers.ValidationError("Due date cannot be in the future.")
        if priority not in ["Low", "Medium", "High"]:
            raise serializers.ValidationError(
                "priority must be either Low, Medium or High."
            )
        return super().validate(attrs)


class TaskStatusSerializer(serializers.ModelSerializer):
    """Serialize the completed_timestamp field of the Task model"""

    class Meta:
        model = Task
        fields = (
            "title",
            "owner",
            "description",
            "due_date",
            "priority_level",
            "status",
            "completed_timestamp",
        )

        read_only_fields = (
            "title",
            "owner",
            "description",
            "due_date",
            "priority_level",
            "completed_timestamp",
        )

        def validate(self, attrs):
            status = attrs.get("status")
            if status not in ["Pending", "Completed"]:
                raise serializers.ValidationError(
                    "Status must be either Pending or Completed"
                )
            return super().validate(attrs)
