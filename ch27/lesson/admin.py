from django.contrib import admin
from lesson.models import reg_model

@admin.register(reg_model)
class reg_modelAdmin(admin.ModelAdmin):
    list_display=("id","fname","lname","email")

# Register your models here.
