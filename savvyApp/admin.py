# admin.py
from django.contrib import admin
from .models import SignUp, Complaints, LogIn

class SignUpAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'address')

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('selectcategory', 'address', 'city', 'state', 'zip', 'landmark','photo')

class LogInAdmin(admin.ModelAdmin):
    list_display=('email','password')


admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Complaints, ComplaintAdmin)
admin.site.register(LogIn,LogInAdmin)