from django.db import models

# Create your models here.
class modelsForm(models.Model):
    Assunto = models.CharField( max_length=50)
    Pergunta = models.TextField( max_length=50)
    Resposta = models.TextField( max_length=50)