from django.db import models
from django.contrib.auth.models import User

class userProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    tipo=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.user.username

class Producto(models.Model):
    producto = models.CharField(max_length=150)
    precio = models.IntegerField(null = True)
    cantidadTotal = models.IntegerField(null = True)
    codigo = models.CharField(max_length=150)

    class Meta:
        db_table = 'producto'

class Detalles(models.Model):
    usuario = models.ForeignKey(userProfile, related_name='userprofile_name', on_delete=models.CASCADE, blank=True, null=True)
    producto = models.ForeignKey(Producto, related_name='producto_name', on_delete=models.CASCADE, blank=True, null=True)
    codigo = models.CharField(max_length=150)
    precio = models.IntegerField(null = True)
    cantidad = models.IntegerField(null = True)

    class Meta:
        db_table = 'detalles'