from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

class Headline(models.Model):
	text = models.CharField(max_length=255)

	def __str__(self):
		return self.text

class Blog(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.title

class Post(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(User, related_name='posts')
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	blog = models.ForeignKey(Blog, related_name='posts')
	slug = models.SlugField(max_length=255, unique=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		is_new = self.pk is None
		if is_new and not self.slug:
			self.slug = slugify(self.title)

		return super().save(*args, **kwargs)
	
	# Adds a "View on Site" button to admin page
	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'slug': self.slug})
		
