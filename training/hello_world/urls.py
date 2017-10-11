from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.home, name='blog_list'),
	url(r'^post/(?P<slug>.+)/$', views.post_view, name='post_detail'),
	url(r'^create-post/$', views.create_post, name='create_post'),

]
