from django.shortcuts import render, redirect
from .form import ContactForm
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            send_mail(
                'Nova Mensagem de Contato',
                form.cleaned_data['mensagem'],
                'seu_email@gmail.com',  # Substitua pelo seu email de envio
                ['patrick.souza@aluno.riogrande.ifrs.edu.br'],  # Substitua pelo email do destinatário
                fail_silently=False,
            )
            return redirect('contact_form') 
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})
