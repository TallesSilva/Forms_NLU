from django.db import models
from django.utils import timezone

from mongoengine import Document, fields

class Form(Document):
    meta = {'strict': False}

    Nome = fields.StringField(required=True)
    Assunto = fields.StringField(required=True)
    Pergunta = fields.StringField(required=True)
    Resposta = fields.StringField(required=True)
