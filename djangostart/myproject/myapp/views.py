from django.shortcuts import render, get_object_or_404
from .models import App, Forblog
from blog.models import Blog

# Create your views here.
def page(request):
    project = App.objects.all()
    blog = Forblog.objects.all()
    return render(request, 'dz/index.html', {'app': project, 'blog': blog})


def blog(request):
    gg=Blog.objects.all()
    return render(request,'blog/blogs.html',{'gg':gg})


def detail(request, blog_id):
    blog2 = get_object_or_404(Blog, pk=blog_id)
    return render(request,'blog/description.html', {'blog':blog2})