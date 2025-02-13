from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """Права только для автора или для чтения"""
    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in permissions .SAFE_METHODS
        )
