from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect

# from django.http import HttpResponse
from .forms import PostForm
from .models import Post

#def home(request):
	#return HttpResponse('hello')

#Using templates
def home(request):
	posts = Post.objects.all().order_by('-date')
	return render(request, 'home.html', {'title': 'Home Page', 'posts': posts})

def post_view(request, slug):
	#try:
		#post = Post.objects.get(slug=slug)
	#except Post.DoesNotExist:
		#raise Http404('Post does not exist')
	post = get_object_or_404(Post, slug=slug)

	return render(request, 'post.html', {
		'title': post.title,
		'post': post
	})

def create_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			# create the post here
			post = form.save()
			return HttpResponseRedirect('blog_list')
	else:
		form = PostForm()

	return render(request, 'create_post.html', {'form':form})
