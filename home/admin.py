from django.contrib import admin
from .models import Tag, Action, Comment, Author

# Register your models here.

admin.site.register(Tag)
admin.site.register(Action)
admin.site.register(Comment)
admin.site.register(Author)
