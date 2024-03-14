from django.contrib import admin
from .models import BlogPost,Category,Match

admin.site.register(Category)
admin.site.register(BlogPost)
admin.site.register(Match)


