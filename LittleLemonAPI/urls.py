from django.urls import path
from . import views

urlpatterns = [
    # Agrega aquí las rutas de tu API
    path('menuitems/', views.MenuItemListView.as_view(), name='menuitem-list'),
    # Agrega más rutas según sea necesario
]
