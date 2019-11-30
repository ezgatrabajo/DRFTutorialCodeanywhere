from rest_framework import permissions

class Isdeveloper(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='Developer'):
            return True
        return False

class Iscliente(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='Cliente'):
            return True
        return False

class Isempresa(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='Empresa'):
            return True
        return False

class Isempleado(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='Empleado'):
            return True
        return False