# myproject/blog/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import rate_post, PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
urlpatterns = [
    path('', include(router.urls)),
    path('rate/<int:post_id>/', rate_post, name='rate-post'),
]
