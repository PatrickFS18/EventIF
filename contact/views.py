
from .formulario import ContactForm  
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect


def contato_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
           
              
            _send_mail(
            'Contato do Evento',
            settings.DEFAULT_FROM_EMAIL,
            form.cleaned_data['email'],
            'contact_email.txt',
            form.cleaned_data
            )
            messages.success(request, 'Inscrição realizada com sucesso!')
            return HttpResponseRedirect('/inscricao/')
    else:
        
        form = ContactForm()
        msg='metodo get, carregou a pagina'
        return render(request, 'contact_form.html', {'form': form,'msg':msg})
    
    

def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])