from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView 
from .serializers import CategorySerializers, SerializersProduit,ProduitSerializersListe,CategorySerializersList
from .models import Product, Category

# Create your views here.
class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    
    
class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = SerializersProduit

    
class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializersList


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProduitSerializersListe
