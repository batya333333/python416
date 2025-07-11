from django.shortcuts import render
from .models import Blog

# Create your views here.
def forblog(request):
    blog = Blog.objects.all()
    return render(request,'blog/blogs.html',{'blog':blog})