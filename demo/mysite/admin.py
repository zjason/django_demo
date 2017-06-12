from django.contrib import admin
from django.db import models
from django.forms import Textarea

from models import Article, Reply

# class ArticleModelAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.Field: {'widget': Textarea(attrs={'row': 10, 'cols': 40})},
#     }

admin.site.register(Article)
admin.site.register(Reply)