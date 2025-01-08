from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, exceptions, views, status, generics, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer, TaskStatusSerializer
from .models import Task
from django.utils import timezone


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(owner=user).order_by("due_date")
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != self.request.user:
            raise exceptions.PermissionDenied(
                "You do not have permissions to access this information."
            )
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != self.request.user:
            raise exceptions.PermissionDenied(
                "You do not have permissions to update this information."
            )
        if instance.status == "Completed":
            raise exceptions.PermissionDenied("You cannot update a completed task.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != self.request.user:
            raise exceptions.PermissionDenied(
                "You do not have permissions to delete this information."
            )
        return super().destroy(request, *args, **kwargs)


class TaskStatusUpdateView(views.APIView):
    serializer_class = TaskStatusSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk, format=None):
        instance = get_object_or_404(Task, pk=pk, owner=request.user)
        if request.data.get("status"):
            serializer = self.serializer_class(
                instance, data=request.data, partial=True
            )
            if serializer.is_valid():
                task = serializer.save()
                if task.status == "Completed":
                    task.completed_timestamp = timezone.now()
                    task.save()
                return Response(
                    {
                        "message": "Status successfully updated.",
                        "data": serializer.data,
                    },
                    status=status.HTTP_200_OK,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["status", "priority_level", "due_date"]
    ordering_fields = ["priority_level", "due_date"]

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(owner=user)
        return queryset
