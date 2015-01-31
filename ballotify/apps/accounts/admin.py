from django.contrib import admin

from authtools.admin import NamedUserAdmin

from models import User


class UserAdmin(NamedUserAdmin):
    pass

admin.site.register(User, UserAdmin)
