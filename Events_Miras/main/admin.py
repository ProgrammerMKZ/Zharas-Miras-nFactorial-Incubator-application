from django.contrib import admin
from .models import Registration_in_event, Event
# Register your models here.
admin.site.register(Registration_in_event)
admin.site.register(Event)