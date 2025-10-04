from django import forms
from .models import Topic, Post, Comment

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'description']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image', 'video', 'audio']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']