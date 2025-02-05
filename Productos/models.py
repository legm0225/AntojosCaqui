from django.db import models

class TipoDetalle(models.Model):
    nombre = models.CharField(max_length=200)
    foto = models.ImageField(null =True, blank=True)

    def __str__(self):
        #Identificar un objeto
        return self.nombre
    
    def numProductos(self):
        pass

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    tipo = models.ForeignKey(TipoDetalle, on_delete=models.CASCADE)
    precio = models.IntegerField()
    descripcion = models.TextField()
    foto = models.ImageField(blank = True, null=True)
    calificacion = models.FloatField(default=0)
   
    @property   #=> convierte un método en un atributo
    def tipoDet(self):
        #infoTipo = {"nombre": "Televisores", "id":2, "foto":None}
        from Productos.serializers import TipoSerial
        return TipoSerial(self.tipo).data

    def __str__(self):
        return self.nombre
    
    def calcularCalificacion(self):
        pass

class Comentario(models.Model):
    usuario = models.CharField(max_length=100)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    calificacion = models.FloatField()
    fecha = models.DateField(auto_now_add=True) #16/09/2021
    #DateTimeField() 16/09/2021 - 3:13:40 p.m.
    #TimeField()
    contenido = models.TextField()

    def __str__(self):
        return self.usuario + " - " + self.producto.nombre

