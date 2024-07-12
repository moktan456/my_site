from django.contrib import admin
from .models import Author,Post,Tag,Comment


# Register your models here.

admin.site.register(Author)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}# to slug automatically
    list_filter = ("author","tag","date")
    list_display=("title","author","date")

class CommentAdmin(admin.ModelAdmin):
    list_display=("user_name","post")
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)
