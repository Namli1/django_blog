from django.contrib import admin
from blog.models import BlogPost, BlogAuthor, BlogComment

# Register your models here.
class BlogPostInline(admin.TabularInline):
    model = BlogPost
    extra = 0

admin.site.register(BlogAuthor)
class BlogAuthorAdmin(admin.ModelAdmin):
    inlines = [BlogPostInline]


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_filter = ('post_date',)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_filter = ('date_of_creation',)

    fieldsets = (
        (None, {
            'fields' : ('title', 'author', 'date_of_creation')
        }),
        ('Blog Post',{
            'fields' : ('text',)
        }),
    )

