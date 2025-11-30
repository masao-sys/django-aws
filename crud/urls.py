from django.urls import path, include
from .views import TopView, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductDetailView

urlpatterns = [
    path('', TopView.as_view(), name='top'),
    path('crud/', ProductListView.as_view(), name='list'),
    path('crud/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('crud/new/', ProductCreateView.as_view(), name="new"),
    path('crud/edit/<int:pk>', ProductUpdateView.as_view(), name="edit"),
    path('crud/delete/<int:pk>', ProductDeleteView.as_view(), name="delete"),
]
