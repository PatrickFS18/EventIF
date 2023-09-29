
from django.contrib import admin
from django.urls import path,include
from core.views import home
from subscriptions.views import new, detail
from contact.views import contact

urlpatterns = [
    path('', home, name='home'),
    path('inscricao/', include('subscriptions.urls')),  
    path("admin/", admin.site.urls),
    path("contact/",contact, name='contact'),

]
