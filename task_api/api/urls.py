from django.urls import path
from accounts.views import CustomUserViewSet
from rest_framework.authtoken import views

urlpatterns = [
    path("users/", CustomUserViewSet.as_view({"get": "list"}), name="user_list"),
    path(
        "users/new/", CustomUserViewSet.as_view({"post": "create"}), name="user_create"
    ),
    path(
        "users/<int:pk>/",
        CustomUserViewSet.as_view({"get": "retrieve"}),
        name="user_detail",
    ),
    path(
        "users/<int:pk>/update/",
        CustomUserViewSet.as_view({"put": "update"}),
        name="user_update",
    ),
    path(
        "users/<int:pk>/delete/",
        CustomUserViewSet.as_view({"delete": "destroy"}),
        name="user_delete",
    ),
    path("login/", views.obtain_auth_token, name="login"),
]
