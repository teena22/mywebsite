from django.contrib import admin
from .models import Msg
class MsgAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email',)
    list_display = ('name', 'email', 'created',)


admin.site.register(Msg, MsgAdmin)

