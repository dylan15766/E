from django.shortcuts import render
from .serializers import BlogSerializer
from .models import Post
from rest_framework import generics
# Create your views here.


def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'templates/post_list.html', {'posts': posts})


class BlogList(generics.ListCreateAPIView):
        queryset = Post.objects.all()
        serializer_class = BlogSerializer
