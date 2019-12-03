from django.db import models


class modelsForm(models.Model):
    Assunto = models.CharField(max_length=50)
    Pergunta = models.TextField(max_length=50)
    Resposta = models.TextField(max_length=50)

    def __str__(self):
        if self.Assunto and self.Pergunta and self.Resposta:
            return "{assunto}: '{pergunta}'? '{resposta}'".format(
                assunto=self.Assunto,
                pergunta=self.Pergunta,
                resposta=self.Resposta
            )
        return "Objeto vazio"
