from django.contrib import admin
from.models import Post, Comment

class ReviewInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    inlines =[
        ReviewInline,
    ]
    list_display = ('body',)

# Register your models here.
admin.site.register(Post,PostAdmin)