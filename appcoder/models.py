from django.db import models

class Curso(models.Model):                  # models.Model es una herencia de la cual hereda toda la clase creada
    nombre=models.CharField(max_length=30)  #permite ingresar un string y SIEMPRE solicita un maximo de longitud
    comision=models.IntegerField()          #permite ingresar un valor numerico entero

class Estudiante(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()                   #permite ingresar un email(sin @ o . no deja guardar)

class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    profesion=models.CharField(max_length=30)

class Entregable(models.Model):
    nombre=models.CharField(max_length=30)
    fecha_de_entrega=models.DateField()    #permite ingresar un tipo de año/mes/dia - DateTimeField es fecha y hora
    email=models.EmailField()
    entregado=models.BooleanField()        #permite ingresar un buleano
