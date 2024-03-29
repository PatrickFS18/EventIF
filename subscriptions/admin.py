from django.contrib import admin
from subscriptions.models import Subscription
from django.utils.timezone import now



class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'cpf', 'created_at', 'subscribed_today']
    date_hierarchy = 'created_at'
    search_fields = ['name', 'email', 'phone', 'cpf', 'created_at', ]
    list_filter = ['created_at',]

    def subscribed_today(self, obj):
        return obj.created_at.date() == now().date()

    subscribed_today.short_description = 'inscrito hoje?'
    subscribed_today.boolean = True
admin.site.register(Subscription, SubscriptionModelAdmin)