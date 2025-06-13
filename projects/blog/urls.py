from django.urls import path
from . import views

app_name ='blogs'

urlpatterns = [
    path('',views.blog_list, name="blog-post"),
    path('new/',views.blog_new, name="blog-new"),
    path('about/',views.about, name="blog-about"),
    path('<slug:slug>', views.blog_page, name="blog-page"),
]
