from django.contrib import admin
from .models import Contact, ContactInfo


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactInfo)
