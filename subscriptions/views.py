from django.http import HttpResponse
from django.shortcuts import render
def subscribe(request):
    return render(request, 'subscriptions/subscription_form.html')