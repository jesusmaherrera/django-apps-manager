from django.contrib import admin
from applications.models import Application, Business, Server

admin.site.register(Application)
admin.site.register(Business)
admin.site.register(Server)