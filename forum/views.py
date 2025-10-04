from django.contrib.auth import login
from .register_form import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Post, Comment
from .forms import TopicForm, PostForm, CommentForm

def forum_home(request):
    topics = Topic.objects.all().order_by('-created_at')
    return render(request, 'forum/forum_home.html', {'topics': topics})

@login_required
def topic_create(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()
            return redirect('forum_home')
    else:
        form = TopicForm()
    return render(request, 'forum/topic_form.html', {'form': form})

def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    posts = topic.posts.all().order_by('created_at')
    return render(request, 'forum/topic_detail.html', {'topic': topic, 'posts': posts})

@login_required
def post_create(request, topic_pk):
    topic = get_object_or_404(Topic, pk=topic_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.topic = topic
            post.save()
            return redirect('topic_detail', pk=topic.pk)
    else:
        form = PostForm()
    return render(request, 'forum/post_form.html', {'form': form, 'topic': topic})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('created_at')
    return render(request, 'forum/post_detail.html', {'post': post, 'comments': comments})

@login_required
def comment_create(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'forum/comment_form.html', {'form': form, 'post': post})