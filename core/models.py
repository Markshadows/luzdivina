from django.db import models
from datetime import datetime

# Create your models here.
class Comunidad(models.Model):
    nombre=models.CharField(max_length=45)
    ubicacion=models.CharField(max_length=45)
    img = models.CharField(max_length=255, default='i3.png')

    def __str__(self):
        return self.nombre
class Sacramento(models.Model):
    nombre=models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

class Coordinador(models.Model):
    nombre=models.CharField(max_length=45)
    appaterno=models.CharField(max_length=45)
    edad=models.CharField(max_length=45)
    comunidad=models.ForeignKey(Comunidad,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class AgentePastoral(models.Model):
    nombre=models.CharField(max_length=45)
    appaterno=models.CharField(max_length=45)
    edad=models.CharField(max_length=45)
    sacramento=models.ForeignKey(Sacramento,on_delete=models.CASCADE)
    comunidad=models.ForeignKey(Comunidad,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' '+ self.appaterno + '-' + self.comunidad.nombre

class MinistroComunion(models.Model):
    nombre=models.CharField(max_length=45)
    appaterno=models.CharField(max_length=45)
    edad=models.CharField(max_length=45)
    comunidad=models.ForeignKey(Comunidad,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Solicitud(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=255)
    fecha = models.DateTimeField(default=datetime.now())
    estado = models.CharField(max_length=45, default='En Espera')
    comunidad=models.ForeignKey(Comunidad,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre +' '+self.estado

class Evento(models.Model):
    nombre=models.ForeignKey(Sacramento,on_delete=models.CASCADE)
    fecha=models.DateTimeField('fecha_evento')
    descripcion=models.CharField(max_length=255)
    comunidad=models.ForeignKey(Comunidad,on_delete=models.CASCADE)
    solicitud=models.ForeignKey(Solicitud,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre.nombre + ' ' + self.descripcion


                