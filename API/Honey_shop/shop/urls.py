from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, OrderViewSet, increment_product_views

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/<int:product_id>',increment_product_views, name='increment_product_views'),
]
