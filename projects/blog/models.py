from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Post(models.Model):

	title = models.CharField(max_length=200)
	content = models.TextField()
	banner = models.ImageField(default='default.jpg',blank=True)
	banner_url = models.URLField(default='',blank=True,null=True)
	author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	slug = models.SlugField(null=True)
	date_posted = models.DateTimeField(auto_now_add= True)


	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title
