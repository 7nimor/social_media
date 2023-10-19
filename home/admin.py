from django.contrib import admin
from home.models import Comments


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'reply', 'post')
