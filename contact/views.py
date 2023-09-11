from .formulario import ContactForm  
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.contrib import messages

def contato_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
                 
            enviar_email(
            'Contato do Evento',
            settings.DEFAULT_FROM_EMAIL,
            form.cleaned_data['email'],
            'contact_email.txt',
            form.cleaned_data
            )
            messages.success(request, 'Mensagem enviada!')
            return redirect('/contact/')
    else:
        
        form = ContactForm()
        msg='metodo get, carregou a pagina'
        return render(request, 'contact_form.html', {'form': form,'msg':msg})
    
    
def enviar_email(dados_contato):
    remetente = dados_contato['email']
    destinatario = ['contato@eventif.com.br', remetente]
    assunto = 'Contato do Evento'
    corpo_mensagem = render_to_string('contact_email.txt', {'dados_contato': dados_contato})
    mail.send_mail(assunto, corpo_mensagem, remetente,[remetente,destinatario])
