from rest_framework.permissions import BasePermission, SAFE_METHODS

"""
Ensures only respective users (i.e. Admins and Reverend)
can perform create/update/delete operations to the RCISA apps. 
"""


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.status == 'ADMIN'

class IsReverend(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.status == 'REVEREND'

class IsMember(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.status == 'MEMBER'

class IsVisitor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.status == 'VISITOR'

class IsAdminOrReverend(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.status in ['ADMIN', 'REVEREND']

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user