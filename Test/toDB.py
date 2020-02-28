from datetime import datetime

from django.shortcuts import render

# Create your views here.
from mongoengine import *
connect('test')

class BlogPost(Document):
    title = StringField(required=True, max_length=200)
    posted = DateTimeField(default=datetime.utcnow)
    tags = ListField(StringField(max_length=50))
    meta = {'allow_inheritance': True}

class TextPost(BlogPost):
    content = StringField(required=True)

class LinkPost(BlogPost):
    url = StringField(required=True)


for post in BlogPost.objects:
    print('===', post.title, '===')
    if isinstance(post, TextPost):
        print(post.content)
    elif isinstance(post, LinkPost):
        print('Link:', post.url)