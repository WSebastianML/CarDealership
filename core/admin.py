from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'db_alias', 'db_host', 'activa']
    list_editable = ['activa']