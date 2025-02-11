from django.shortcuts import render

posts = [
			{
				'author':'Dibik',
				'title':'blog-post1',
				'content':'First post content',
				'date_posted':'August 20'
			},
			{
				'author':'Jane Doe',
				'title':'blog-post2',
				'content':'Second post content',
				'date_posted':'August 21'
			},
		]

def blog(request):
	context ={'posts':posts}
	return render(request,'blog/blog.html',context)

def about(request):
	return render(request,'blog/about.html',{'title':'About'})
