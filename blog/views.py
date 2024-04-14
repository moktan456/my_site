from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'blog/index.html')
    # return HttpResponse('Working from root')

def allPosts(request):
    return HttpResponse("All posts page working")

def post_detail(request):
    pass
