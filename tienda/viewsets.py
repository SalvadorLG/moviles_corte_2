from rest_framework import viewsets
from tienda.models import Producto, Detalles
from tienda.serializers import ProductosSerializer, DetallesSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductosSerializer

class DetallesViewSet(viewsets.ModelViewSet):
    queryset = Detalles.objects.all()
    serializer_class = DetallesSerializer