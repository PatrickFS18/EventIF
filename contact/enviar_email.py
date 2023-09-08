from django.core.mail import send_mail
from django.template.loader import render_to_string

def enviar_email(dados_contato):
    remetente = dados_contato['email']
    destinatario = ['contato@eventif.com.br', remetente]

    assunto = 'Contato do Evento'
    corpo_mensagem = render_to_string('contact_email.txt', {'dados_contato': dados_contato})

    send_mail(assunto, corpo_mensagem, remetente, destinatario)
    