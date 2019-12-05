from django.db import models

USA = 'usa'
FRANCE = 'france'
CHINA = 'china'
GERMANY = 'germany'
SPAIN = 'spain'

TOPICS = (
    (USA, 'USA'),
    (FRANCE, 'France'),
    (CHINA, 'China'),
    (GERMANY, 'Germany'),
    (SPAIN, 'Spain'),
        )

class ModeloFormulario(models.Model):
    Assunto = models.CharField(choices=TOPICS, max_length=50)
    Pergunta = models.TextField(max_length=1000)
    Resposta = models.TextField(max_length=1000)

    def __str__(self):
        if self.Assunto and self.Pergunta and self.Resposta:
            return "{assunto}: '{pergunta}'? '{resposta}'".format(
                assunto=self.Assunto,
                pergunta=self.Pergunta,
                resposta=self.Resposta
            )
        return "Objeto vazio"
    
