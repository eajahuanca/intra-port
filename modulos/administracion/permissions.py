from rest_framework.permissions import DjangoModelPermissions


class BaseModelPermission(DjangoModelPermissions):
    def has_permission(self, request, view):
        return super(BaseModelPermission, self).has_permission(request, view)


class IsPersonUserPermission(DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        persona_id = getattr(user, 'persona_id', None)
        setattr(view, 'persona_id', persona_id)
        return persona_id is not None
