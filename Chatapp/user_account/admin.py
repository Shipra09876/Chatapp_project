from django.contrib import admin
from user_account.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["id","username","email", "first_name","last_name","tc","is_admin"]
    
    list_filter = ["is_admin"]
    fieldsets = [
        ('User Credentials', {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["username","first_name","last_name","tc"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["username","email", "first_name","last_name", "tc","password1", "password2"],
            },
        ),
    ]
    search_fields = ["id","username","email"]
    ordering = ["id","email"]
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)
# Register your models here.
