from django.contrib import admin
from .models import Registration_on_event, Event
# Register your models here.
admin.site.register(Registration_on_event)
admin.site.register(Event)