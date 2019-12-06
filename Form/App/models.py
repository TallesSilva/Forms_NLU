from django.db import models

FAQKYROS = 'INFORMAÇÃO DA EMPRESA'
FAQCONTATO = 'IMFORMAÇÃO DE CONTATO'
FAQLOCAL = 'INFORMAÇÃO DO LOCAL'
FAQPRODUTOS = 'INFORMAÇÃO DO PRODUTO'
CHITCHAT = 'COMUNICAÇÃO FORA DE CONTEXTO'

TOPICS = (
    (FAQKYROS, 'INFORMAÇÃO DA EMPRESA'),
    (FAQCONTATO, 'IMFORMAÇÃO DE CONTATO'),
    (FAQLOCAL, 'INFORMAÇÃO DO LOCAL'),
    (FAQPRODUTOS, 'INFORMAÇÃO DO PRODUTO'),
    (CHITCHAT, 'COMUNICAÇÃO FORA DE CONTEXTO'),
        )

class ModeloFormulario(models.Model):
    Checkbox = models.NullBooleanField(default=None)
    Assunto = models.CharField(choices=TOPICS, max_length=50)
    Pergunta = models.TextField(max_length=1000)
    Resposta = models.TextField(max_length=1000)

    def __str__(self):
        if self.Assunto and self.Pergunta and self.Resposta:
            return "{assunto}: '{pergunta}'? '{resposta}'".format(
                checkbox=self.Checkbox,
                assunto=self.Assunto,
                pergunta=self.Pergunta,
                resposta=self.Resposta
            )
        return "Objeto vazio"

