from django.contrib import admin

from my_app.models import form_data
@admin.register(form_data)
class form_dataAdmim(admin.ModelAdmin):
    list_display=("id","fname","lname","pwd","email")

# Register your models here.
