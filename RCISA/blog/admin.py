from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'like_count_display', 'share_count', 'created_at', 'updated_at')
    list_filter = ('author__status', 'author__congregation', 'created_at')
    search_fields = ('title', 'content', 'author__full_name')
    readonly_fields = ('slug', 'like_count_display', 'share_count')

    def like_count_display(self, obj):
        return obj.likes.count()

    like_count_display.short_description = "Likes"


admin.site.register(BlogPost, BlogPostAdmin)