from django.contrib import admin
from .models import UserRegistration
# Register your models here.
@admin.register(UserRegistration)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','passcode',)