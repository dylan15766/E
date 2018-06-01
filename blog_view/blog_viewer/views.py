# Create your views here.
from django.shortcuts import render
from django.views import View
import requests


class Finder(View):

    def get(self, request, *args, **kwargs):
        #getted = requests.get('blog:8001/api/blog/')
        getted = requests.get('http://blog:8000/api/blog/')
        return render(request, 'post_list.html', {'posts': getted.json()})
