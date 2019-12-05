from django import forms
from .models import Comment, Post

class EmailPostForm(forms.Form):
	name = forms.CharField(max_length=25)
	email = forms.EmailField()
	to = forms.EmailField()
	comments = forms.CharField(required=False,widget=forms.Textarea)

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'body')

		
class PostForm(forms.ModelForm):
	class Meta: 
		model = Post
		fields = ('title', 'body', 'tags')
		widgets = {
			'title' : forms.TextInput(attrs = {
			'class': 'form-control',
			'placeholder': 'Title'}),

			'body' : forms.Textarea(attrs = {
			'class': 'form-control',
			'placeholder': 'Email'}),

			'tags' : forms.TextInput(attrs = {
			'class': 'form-control',
			'placeholder': 'Tags'
			}),
		}