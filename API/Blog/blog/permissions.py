from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Foydalanuvchiga faqat o'zining postlarini o'zgartirish huquqini beradi.
    """
    def has_object_permission(self, request, view, obj):
        # Foydalanuvchi faqat o'zining postlarini o'zgartirishi mumkin
        if request.method in permissions.SAFE_METHODS:
            return True
        # Foydalanuvchi ro'yxatdan o'tgan yoki postni yaratgan foydalanuvchisi degan shart qo'shing
        return obj.author == request.user or obj.author is None
