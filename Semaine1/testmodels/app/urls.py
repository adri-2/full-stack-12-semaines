from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (CategoryCreateView,
                    CategoryListView,
                    CategoryDetailView,
                    CategoryDeleteView,
                    SupplierViewSet,ClientViewSet,ProductViewApi
                    )
router = DefaultRouter()
router.register(r'suppliers',SupplierViewSet, basename='supplier')
router.register(r'client',ClientViewSet, basename='client')
router.register(r'product',ProductViewApi, basename='product')

urlpatterns=[
    path('categorie/create/',CategoryCreateView.as_view(),name='categorie-create'),
     path('categorie/list/',CategoryListView.as_view(),name='categorie-list'),
     path('categorie/<int:pk>/',CategoryDetailView.as_view(),name='category-detail'),
     path('categorie/delete/<int:pk>/',CategoryDeleteView.as_view(),name='categorie-delete'),
     path('v2/',include(router.urls)),
    
]