
from django.shortcuts import render, redirect
from .formulario import ContactForm  
from .enviar_email import enviar_email  

def contato_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
           
            enviar_email(form.cleaned_data)  

            msg='success, testando'
            return redirect('contato_form.html',{'msg':msg})  
    else:
        form = ContactForm()
    msg='erro, testando'
    return render(request, 'contato_form.html', {'form': form,'msg':msg})