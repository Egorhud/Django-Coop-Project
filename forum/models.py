
from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')

	def __str__(self):
		return self.title

class Post(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	content = models.TextField()
	image = models.ImageField(upload_to='forum_images/', blank=True, null=True)
	video = models.FileField(upload_to='forum_videos/', blank=True, null=True)
	audio = models.FileField(upload_to='forum_audio/', blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.author.username}: {self.content[:30]}"

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.author.username}: {self.content[:30]}"
