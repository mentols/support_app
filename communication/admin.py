from django.contrib import admin

from communication.models import Ticket

admin.site.register(Ticket)


class ProjectImageAdmin(admin.ModelAdmin):
    list_display = [Ticket, 'status']
    fields = ['id', 'status']
    list_editable = ['status']
