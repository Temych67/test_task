from django.contrib import admin
from blog.models import BlogPostDB


class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'date','author')
	search_fields = ('title','author')

	ordering = ('date',)
admin.site.register(BlogPostDB, BlogPostAdmin)
