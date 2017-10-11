from django.contrib import admin

#from .models import Headline, Blog, Post
from . import models

@admin.register(models.Headline)
class HeadlineAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'description')

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'body', 'date', 'author_first_name')
	list_filter = ('author',) # Must have trailing comma if single item
	date_hierarchy = 'date' # No brackets as can only have one field
	search_fields = ('title', 'slug', 'body', 'author__username') #author is an object so needs 		double underscore
	fieldsets = [
		(None, {
			'fields': ('title', 'slug', 'blog')
		}),
		('Content', {
			'fields': ('body',)
		}),
		('Metadata', {
			'fields': ('author',),
			'classes': ('wide', 'collapse'),
		})
    	]
	prepopulated_fields = {"slug": ("title",)}
	
	def author_first_name(self, obj):
		return obj.author.first_name
