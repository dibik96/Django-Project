from django.urls import path
from . import views

urlpatterns = [
    path('',views.blog, name="blog-post"),
    path('about/',views.about, name="blog-about"),
]
