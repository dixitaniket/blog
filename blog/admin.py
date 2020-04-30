from django.contrib import admin
from blog.models import *
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)

admin.site.register(UserProfileInfo)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

# Register your models here.
