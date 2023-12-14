from django.shortcuts import render

# Create your views here.
# Create your views here.


from django.views.generic import ListView
from .models import Markaz, Kurslar, Xizmatlar, Galereya, Jamoa,  Blog


class BizViews(ListView):
    model = Markaz
    template_name = "about.html"
    context_object_name = "Markaz"
    
    
class BlogViews(ListView):
    model = Blog
    template_name = "blog.html"
    context_object_name = "Blog"
    
def blog_detail(request,id):    
    blogs=Blog.objects.get(id=id)
    blogs.viewed=blogs.viewed+1
    blogs.save()
    return render(request,'blog.html',{"blogs":blogs})

# class VideoViews(ListView):
#     model = VideoKontent
#     template_name = "video.html"
#     context_object_name = "Video"
    
def index(request):
    markaz = Markaz.objects.all()
    kurslar = Kurslar.objects.all()
    xizmatlar = Xizmatlar.objects.all()
    galereya = Galereya.objects.all()
    jamoa = Jamoa.objects.all()
    # bitiruvchi = Bitiruvchi.objects.all()
    blog = Blog.objects.all()
    contex = {
        'Markaz':markaz,
        'Kurslar':kurslar,
        'Xizmatlar':xizmatlar,
        'Jamoa':jamoa,
        # 'Bitiruvchi':bitiruvchi,
        'Galereya':galereya,
        'Blog':blog,
    }
    return render(request, ['index.html','blog.html'] , contex)