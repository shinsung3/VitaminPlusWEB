from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

from .models import ChatData

# Register your models here.
class ChatDataAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(ChatData, ChatDataAdmin)