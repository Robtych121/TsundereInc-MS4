from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile


class Inline(admin.StackedInline):
    """
    Taken from Django project docs
    Define an inline admin descriptor for profile model
    which acts a bit like a singleton
    """
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (Inline, )


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
