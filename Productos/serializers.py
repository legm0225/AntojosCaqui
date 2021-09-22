from rest_framework import serializers

from Productos.models import *

class TipoSerial(serializers.ModelSerializer):
    class Meta:
        model = TipoDetalle
        fields = '__all__'
        #fields = ["nombre", "foto"]

class ProductoSerial(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class ComentarioSerial(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'
