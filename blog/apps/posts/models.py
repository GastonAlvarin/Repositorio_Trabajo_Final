from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):

	titulo = models.CharField(max_length=200)
	contenido = models.TextField(max_length=800)
	fecha_creacion = models.DateTimeField(default=timezone.now)
	

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name =("Post")
		verbose_name_plural =("Posts")

class Comentario(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	contenido = models.TextField(max_length=800)
	fecha_hora = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.contenido

	class Meta:
		verbose_name = ("Comentario")
		verbose_name_plural = ("Comentarios")

#class Cont_Comentario():

  #def __init__(self, inicial=0):
    #self.numero = inicial

  #def siguiente(self):
    #self.numero += 1
    #return self.numero