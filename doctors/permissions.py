from rest_framework import permissions


class IsDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        # request.user = usuario logueado | groups = lista de grupos | buscar grupo "doctors"
        return request.user.groups.filter(
            name="doctors"
        ).exists()  # retorna un booleano
