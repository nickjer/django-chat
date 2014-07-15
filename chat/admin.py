from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from chat.models import Msg

class MsgInline(admin.TabularInline):
    model = Msg
    extra = 0
    fields = ['msg_text']

class AuthorAdmin(UserAdmin):
    inlines = [MsgInline]

admin.site.unregister(User)
admin.site.register(User, AuthorAdmin)
