from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from subscriptions.forms import SubscriptionForm
from django.core import mail
from django.template.loader import render_to_string
from django.http import HttpResponse  # Import necessário
from django.conf import settings
from subscriptions.models import Subscription
from django.shortcuts import resolve_url as r

def new(request):
    if request.method=='POST':
        return create(request)


    return empty_form(request)



def empty_form(request):
    return render(request, 'subscriptions/subscription_form.html',  {'form': SubscriptionForm()})


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form':form})
    sub = Subscription.objects.create(**form.cleaned_data)
    _send_mail('Confirmação de inscrição', settings.DEFAULT_FROM_EMAIL, sub.email, 'subscriptions/subscription_email.txt', {'subscription':sub})

    return HttpResponseRedirect(r('subscriptions:detail', sub.pk))

def detail(request, pk):
    try: 
        sub = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        raise Http404
    return render(request, 'subscriptions/subscription_detail.html', {'subscription': sub})


def _send_mail(subject, from_, to, template_name, context):
     body = render_to_string(template_name, context)
     mail.send_mail(subject, body, from_,  [from_, to])

