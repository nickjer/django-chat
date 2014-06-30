from django.contrib import admin

from chat.models import Msg, Author

class MsgInline(admin.TabularInline):
    model = Msg
    extra = 0
    fields = ['msg_text']

class AuthorAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = [MsgInline]

admin.site.register(Author, AuthorAdmin)
