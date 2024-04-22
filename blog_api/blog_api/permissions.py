from rest_framework import permissions

class IsAuthorOrReadonly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #faqat ko'rish uchun
        if request.method in permissions.SAFE_METHODS:
            return True
        #o'zgartirish faqat muallif uchun 
        return obj.author == request.user