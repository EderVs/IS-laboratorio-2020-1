from django.contrib import admin

from .models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email',)


admin.site.register(Subscriber, SubscriberAdmin)