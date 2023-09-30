from django.db import models

class J_favoritos(models.Model):
  Title = models.CharField(max_length=50)
  Dev = models.CharField(max_length=50)
  Likes = models.CharField(max_length=50)
  Dislikes = models.CharField(max_length=50)

class J_recomendados(models.Model):
  Title = models.CharField(max_length=50)
  Dev = models.CharField(max_length=50)
  Likes = models.CharField(max_length=50)
  Dislikes = models.CharField(max_length=50)
