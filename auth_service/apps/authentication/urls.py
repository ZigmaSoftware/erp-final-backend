from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.authentication.views.auth import LoginView, LoginPageView, TokenRefreshView
from apps.authentication.views.permission_and_role import (
    PermissionListView,
    MasterPermissionsView,
    UserRoleViewSet,
    UserRolePermissionsView,
    GroupPermissionViewSet,
)
from apps.authentication.views.user import UserViewSet

# Create router for ViewSets
router = DefaultRouter()
router.register(r"roles", UserRoleViewSet, basename="user-role")
router.register(r"group-permissions", GroupPermissionViewSet, basename="group-permission")
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    # Auth endpoints
    path("login/", LoginView.as_view(), name="auth-login"),
    path("login_page/", LoginPageView.as_view(), name="auth-login-page"),
    path("refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    
    # Permission endpoints
    path("permissions/", PermissionListView.as_view(), name="permission-list"),
    path("permissions/master/", MasterPermissionsView.as_view(), name="master-permissions"),
    
    # Role endpoints (via router)
    path("", include(router.urls)),
    
    # Role permissions endpoints
    path("roles/<uuid:role_id>/permissions/", UserRolePermissionsView.as_view(), name="role-permissions"),
]

