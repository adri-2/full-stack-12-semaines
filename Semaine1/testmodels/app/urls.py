from django.urls import path
from .views import CategoryCreateView,CategoryListView,CategoryDetailView,CategoryDeleteView

urlpatterns=[
    path('categorie/create/',CategoryCreateView.as_view(),name='categorie-create'),
     path('categorie/list/',CategoryListView.as_view(),name='categorie-list'),
     path('categorie/<int:pk>/',CategoryDetailView.as_view(),name='categorie-detail'),
     path('categorie/delete/<int:pk>/',CategoryDeleteView.as_view(),name='categorie-delete'),
    
]