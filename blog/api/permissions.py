from rest_framework import permissions


class AuthorModifyOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True

    return request.user == obj.author


# IsAdminUser subclassed when combining permissions
# Because DRF does not know how to check permissions for a user-created object.
class IsAdminUserForObject(permissions.IsAdminUser):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_staff)    