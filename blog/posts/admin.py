from django.contrib import admin
from .models import Category, Topic, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic_with_category', 'created_by', 'created_at')
    readonly_fields = ('created_at',)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('topic', 'topic__category', 'created_by')
    @admin.display(description='Topic (Category)')
    def topic_with_category(self, obj):
        return f"{obj.topic.name} ({obj.topic.category.name})"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('name', 'category')
