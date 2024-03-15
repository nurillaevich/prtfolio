from django.contrib import admin
from .models import Portfolio, Services, Categories, About


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Services)
admin.site.register(Categories)
admin.site.register(About)
