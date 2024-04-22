from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .models import Product, Order
from .serializers import ProductSerializer,OrderSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def increment_product_views(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.most_viwed += 1
    product.save()
    print(product)
    return HttpResponse({product.most_viwed})


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
