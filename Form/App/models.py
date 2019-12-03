from django.db import models

# Create your models here.
class modelsForm(models.Model):
    Assunto = models.CharField(blank=True, max_length=50)
    Pergunta = models.CharField(blank=True, max_length=50)
    Resposta = models.CharField(blank=True, max_length=50)