from django.contrib import admin
from .models import Post

class MyAdmin(admin.ModelAdmin):
    list_display = ('title','author','date_posted')
    search_fields = ('title',)

admin.site.register(Post, MyAdmin)



