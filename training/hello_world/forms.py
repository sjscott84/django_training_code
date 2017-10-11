from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ('slug', 'date') 
		#fields = '__all__' #[field1, field2, field3]
