from django.shortcuts import render
from rest_framework import generics
from .models import Category, MenuItem, Order
from .serializers import CategorySerializer, MenuItemSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated



class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Usuarios autenticados o lectura para todos

class MenuItemListView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['category']  # Para filtrar por categoría
    ordering_fields = ['price']  # Para ordenar por precio


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Asignar el usuario automáticamente

