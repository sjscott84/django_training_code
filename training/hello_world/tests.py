from django.test import TestCase
from django.contrib.auth.models import User

from .models import Blog, Post

class BlogTest(TestCase):
	#Factory Boy - library to create fixtures
	
	#Setup runs before every method 
	def setUp(self):
		self.user = User.objects.create(username='foo')
		self.user.set_password('password')
		self.user.save()

	#Must be called test_something
	def test_home(self):
		response = self.client.get('/blog/')
		self.assertEqual(response.status_code, 200)

	def test_post_notfound(self):
		response = self.client.get('/blog/post/non-existant/')
		self.assertEqual(response.status_code, 404)

	def test_post_found(self):
		blog = Blog.objects.create(title="a blog")
		post = Post.objects.create(title='A test', author=self.user, body='This is a test', blog=blog)
		response = self.client.get('/blog/post/{}/'.format(post.slug))
		self.assertEqual(response.status_code, 200)

		#To Programatically log in a user
		#self.client.login(username=self.user.username, password='password')
	
	#Test if we have log in functionality
	def test_create_post_login_redirect(self):
		response = self.client.get('/blog/create-post/')
		self.assertEqual(response.status_code, 302)

	def test_create_post_logging_in(self):
		self.client.login(username=self.user.username, password='password')
		response = self.client.get('/blog/create-post/')
		self.assertEqual(response.status_code, 200)

