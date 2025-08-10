from django.contrib import admin
from .models import Sermon


class SermonAdmin(admin.ModelAdmin):
    list_display = ('title', 'preacher', 'date_preached', 'created_at', 'updated_at', 'like_count', 'share_count')
    list_filter = ('date_preached', 'preacher')
    search_fields = ('title', 'description', 'preacher__full_name')
    readonly_fields = ('slug', 'created_at', 'updated_at', 'share_count', 'like_count')

    def like_count(self, obj):
        return obj.likes.count()
    like_count.short_description = 'Likes'


admin.site.register(Sermon, SermonAdmin)