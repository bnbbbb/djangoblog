from django.contrib import admin
from .models import Post, Tag, Comment, Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tag)