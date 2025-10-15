from django.shortcuts import render,get_object_or_404
from django.db.models import Max
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView,CreateAPIView
from rest_framework.views import APIView
from .models import Product,OrderItem,Order
from .serializers import ProdutSerializer,OrderItemSerializer,OrderSerializer,ProductInfoSerializer
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class ProductPagination(PageNumberPagination):
    page_size=10
    page_size_query_param='page_size'
class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProdutSerializer
    search_fields=['name','price']
    filterset_fields =['name','price']
    
    ordering_fields=['name','price','stock']

class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProdutSerializer

class OrderListView(ListAPIView):
    queryset = Order.objects.prefetch_related('items','items__product').all()
    serializer_class = OrderSerializer

@api_view(['GET'])
def product_info(request):
    products = Product.objects.all()
    serializer=ProductInfoSerializer(
        {'products':products,'count':len(products),
         'max_price':products.aggregate(max_price=Max('price'))['max_price']})
    return Response(serializer.data)
