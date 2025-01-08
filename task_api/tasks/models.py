from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Task(models.Model):
    """Define the attributes of a task"""

    PRIORITY_CHOICES = (("Low", "Low"), ("Medium", "Medium"), ("High", "High"))

    STATUS_CHOICES = (("Pending", "Pending"), ("Completed", "Completed"))

    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    description = models.TextField()
    due_date = models.DateField()
    priority_level = models.CharField(
        choices=PRIORITY_CHOICES, default="Low", max_length=10
    )
    status = models.CharField(choices=STATUS_CHOICES, default="Pending", max_length=15)
    completed_timestamp = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
