from django.contrib import admin
from django.contrib.admin.models import LogEntry

from .models import Timeslot

admin.site.register(Timeslot)
admin.site.register(LogEntry)
