from rest_framework import permissions
from rest_framework.permissions import  SAFE_METHODS
from .constants import  *





class IsOwner(permissions.BasePermission):
    message =NO_REQUIRED_PERMISSIONS

    def has_object_permission(self, request, view, obj):
        return request.user.profile == obj.profile




class SuperuserOrGetOnly(permissions.BasePermission):

	def has_permission(self,request,view):
		if (request.method in SAFE_METHODS) or request.user.is_superuser==True:
			return request.user