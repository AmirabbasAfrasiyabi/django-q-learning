from django.contrib import admin
from .models import Post, Comment


class CommentInlineAdmin(admin.StackedInline):
    model = Comment
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInlineAdmin]

    list_display = ['id', 'title', 'author_first_name', 'author', 'accepted']
    search_fields = ['=title', 'id', 'author__username', 'author__first_name']
    list_filter = ['author', 'created_date', 'accepted']

    readonly_fields = ('id', 'created_date' , )          # ← removed 'author' from readonly

    fieldsets = (
        ('basic data', {
            'fields': ('id', 'created_date', 'accepted')
        }),
        ('post info', {
            'fields': ('title', 'content', 'author', 'release_date')   # ← added 'author' here (visible)
        }),
    )

    actions = ['accept_posts']

    def author_first_name(self, post):
        return post.author.first_name if post.author else '-'

    def save_model(self, request, obj, form, change):
        """
        Automatically set author to current user when creating (not editing)
        """
        if not change:                    # Only on creation (not on update)
            obj.author = request.user
        super().save_model(request, obj, form, change)

    def accept_posts(self, request, queryset):
        queryset.update(accepted=True)    # ← more efficient than loop + save()

    accept_posts.short_description = 'Mark selected posts as accepted'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'post', 'created_date', 'status']
    list_filter = ['status']
    raw_id_fields = ['post']