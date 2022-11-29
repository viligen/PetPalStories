from django.contrib import admin

from PetPalStories.forum.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'owner', 'published_on',)
    list_filter = ('id', 'topic', 'owner', 'published_on',)
    search_fields = ('topic__startswith', 'topic__endswith', 'owner__username')
    ordering = ('id', 'topic', 'owner', 'published_on',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'owner', 'parent_post', 'published_on',)
    list_filter = ('id', 'text', 'owner', 'parent_post', 'published_on',)
    search_fields = ('text__startswith', 'text__endswith', 'owner__username', 'parent_post__topic')
    ordering = ('id', 'text', 'owner', 'parent_post', 'published_on',)