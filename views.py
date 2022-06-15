from django.shortcuts import render

from library.models import Home

# Create your views here.
def index(request):
    post = Home.objects.all
    ps = {'post':post} 
    return render(request,'index.html',ps)

def detail(request):
    post= Home.objects.all
    p ={'post':post}
  
    return render(request,'details.html', p)