from django.contrib import admin
from student.models import profile


class profileAdmin(admin.ModelAdmin):
    list_display=('name','email','id')

admin.site.register(profile,profileAdmin)

# Register your models here.
