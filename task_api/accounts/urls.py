from django.urls import path
from .views import CustomUserViewSet
from rest_framework.authtoken import views

urlpatterns = [
    path("", CustomUserViewSet.as_view({"get": "list"}), name="user_list"),
    path("new/", CustomUserViewSet.as_view({"post": "create"}), name="user_create"),
    path(
        "<int:pk>/",
        CustomUserViewSet.as_view({"get": "retrieve"}),
        name="user_detail",
    ),
    path(
        "<int:pk>/update/",
        CustomUserViewSet.as_view({"put": "update"}),
        name="user_update",
    ),
    path(
        "<int:pk>/delete/",
        CustomUserViewSet.as_view({"delete": "destroy"}),
        name="user_delete",
    ),
    path("login/", views.obtain_auth_token, name="login"),
]
