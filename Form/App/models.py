from django.db import models

ask_faqkyros = 'ask_faq/kyros'
ask_faqowners_kyros = 'ask_faq/owners_kyros'
ask_faqfoundation = 'ask_faq/foundation'
ask_faqservices = 'ask_faq/services'
ask_faqprojects = 'ask_faq/projects'
ask_faqproducts = 'ask_faq/products'
ask_faqkyros_vision = 'ask_faq/kyros_vision'
ask_faqkyros_values = 'ask_faq/kyros_values'
ask_faqkyros_address = 'ask_faq/kyros_address'
ask_faqkyros_contact = 'ask_faq/kyros_contact'
ask_faqkyros_email = 'ask_faq/kyros_email'

TOPICS = (
    (ask_faqkyros, 'INFORMAÇÃO DA EMPRESA'),
    (ask_faqowners_kyros, 'INFORMA PROPRIETÁRIOS'),
    (ask_faqfoundation, 'INFORMA FUNDAÇÃO'),
    (ask_faqservices, 'INFORMA OS SERVIÇOS'),
    (ask_faqprojects, 'INFORMA OS PROJETOS'),
    (ask_faqproducts, 'INFORMA PRODUTOS'),
    (ask_faqkyros_vision, 'INFORMA VISÃO DA EMPRESA'),
    (ask_faqkyros_values, 'INFORMA VALORES'),
    (ask_faqkyros_address, 'INFORMA ENDEREÇO'),
    (ask_faqkyros_contact, 'INFORMA CONTATO'),
    (ask_faqkyros_email, 'INFORMA EMAIL'),
        )

class ModelFormulario(models.Model):
    Assunto = models.CharField(choices=TOPICS, max_length=20)
    Pergunta = models.CharField(blank=True, max_length=50)
    Resposta = models.CharField(blank=True, max_length=50)

    def __str__(self):
        if self.Assunto and self.Pergunta and self.Resposta:
            return "{assunto}: '{pergunta}'? '{resposta}'".format(
                assunto=self.Assunto,
                pergunta=self.Pergunta,
                resposta=self.Resposta
            )
        return "Objeto vazio"

