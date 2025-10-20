from django.shortcuts import render,get_object_or_404
from django.db.models import Max
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import generics
from rest_framework.views import APIView
from .models import Product,OrderItem,Order
from .serializers import ProdutSerializer,OrderItemSerializer,OrderSerializer,ProductInfoSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny

# Create your views here.

# class ProductPagination(PageNumberPagination):
#     page_size=10
#     page_size_query_param='page_size'
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProdutSerializer
    # search_fields=['name','price']
    # filterset_fields =['name','price']
    
    # ordering_fields=['name','price','stock']

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProdutSerializer
    
    def get_permissions(self):
        self.permission_classes=[AllowAny]
        if self.request.method == 'POST':
            self.permission_classes =[IsAdminUser]
        return super().get_permissions()
   

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProdutSerializer
    lookup_url_kwarg='product_id'
    

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items','items__product').all()
    serializer_class = OrderSerializer
    
class UserOrderListView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items','items__product').all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # user = self.request.user
        qs=super().get_queryset()
        return qs.filter( user = self.request.user) 

# @api_view(['GET'])
# def product_info(request):
#     products = Product.objects.all()
#     serializer=ProductInfoSerializer(
#         {'products':products,'count':len(products),
#          'max_price':products.aggregate(max_price=Max('price'))['max_price']})
#     return Response(serializer.data)

class ProductInfoAPIView(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer=ProductInfoSerializer(
            {'products':products,'count':len(products),
            'max_price':products.aggregate(max_price=Max('price'))['max_price']})
        return Response(serializer.data)
        
