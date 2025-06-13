from django.shortcuts import render
from .forms import NewPostForm
from .models import Post
from django.contrib.auth.decorators import login_required

# TODO: Not using this list
# posts = [
# 			{
# 				'author':'Dummy',
# 				'title':'blog-post1',
# 				'content':'First post content',
# 				'date_posted':'August 20'
# 			},
# 			{
# 				'author':'Jane Doe',
# 				'title':'blog-post2',
# 				'content':'Second post content',
# 				'date_posted':'August 21'
# 			},
# 		]

def about(request):
	return render(request,'blog/about.html',{'title':'About'})

def blog_list(request):
	posts = Post.objects.all().order_by('-date_posted')
	return render(request,'blog/blog_list.html',{'posts':posts,'title':'Posts'})

def blog_page(request,slug):
	post = Post.objects.get(slug=slug)
	return render(request,'blog/blog_page.html',{'post':post,'title':f'Page-{slug}'})


@login_required
def blog_new(request):
	if request.method == "POST":
		form = NewPostForm()
	else:
		form = NewPostForm()
	return render(request,'blog/blog_new.html',{'form':form,'title':'New Post'})
