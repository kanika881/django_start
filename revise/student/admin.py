from django.contrib import admin
from student.models import register_d,Login
class register_dAdmin(admin.ModelAdmin):
    list_display=("name","user_id","email")

admin.site.register(register_d,register_dAdmin)
@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display=("user_id",)
    

# Register your models here.
