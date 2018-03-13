from __future__ import unicode_literals
from django.contrib import admin
from django.db import models


# create the blog model

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return self.title


# set the admin page for BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')


# register the model (especially important

admin.site.register(BlogPost)
