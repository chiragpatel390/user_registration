from django.contrib import admin
from user.models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'user', 'compressed_url', 'url')
    search_fields = ['id', 'compressed_url', 'url']
