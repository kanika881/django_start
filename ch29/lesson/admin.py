from django.contrib import admin
from .models import formmodel

@admin.register(formmodel)
class formmodelAdmin(admin.ModelAdmin):
    list_display=("name","email")

