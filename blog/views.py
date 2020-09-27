from django.shortcuts import render,HttpResponse

def blog(request):
    n = (1,2,3)
    return render(request,'blog/blog.html',{'img' : n})