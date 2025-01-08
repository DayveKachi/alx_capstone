from django.shortcuts import render
from rest_framework import viewsets, status, exceptions
from .serializers import CustomUserSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = get_user_model().objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {"message": "Registration successful", "token": token.key},
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "User updated successfully", "data": serializer.data},
            status=status.HTTP_200_OK,
        )

    # def destroy(self, request, *args, **kwargs):
    #     user = request.user
    #     if not user.is_superuser:
    #         raise exceptions.PermissionDenied(
    #             "You do not have permissions to delete this user."
    #         )
    #     return super().destroy(request, *args, **kwargs)
