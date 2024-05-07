from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import MoreInfo
class MoreInfo(admin.StackedInline):
    model = MoreInfo
class extendUser(UserAdmin):
    
    inlines = (MoreInfo, )
    # list_display = ("address", "phone" )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
    )

admin.site.unregister(User)
admin.site.register(User, extendUser)
