from django.shortcuts import render, HttpResponseRedirect, Http404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse
from .forms import LoginForm
from news.models import Author, News, MainNews, Files, AllFiles, AllWebs, Webs, Pictures, Gallery
from django.contrib.auth.decorators import login_required
# Create your views here.



def logout_view(request):
    logout(request)
    return HttpResponseRedirect('%s' % reverse('login'))

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect('/panel/')
    else:
        pass
    
    context={"form":form,}
    return render(request, "login.html", context)

@login_required
def user_news_view(request):
    qs = News.objects.order_by('-timestamp')
    qs2 = MainNews.objects.all()
    
    
        
    context={'news':qs, 'mainnews':qs2 }
    return render(request, "panel.html", context)

@login_required
def user_view(request):
    username = Author.objects.get(user = request.user)
    if username.username:
        username = username.username
    else:
        username = username.user.username
        
    context={'username':username,}
    return render(request, "main-panel.html", context)


@login_required
def user_gallery_view(request):
    qs = Gallery.objects.order_by('-timestamp')
    
    
    
        
    context={'gallery':qs }
    return render(request, "gallery-panel.html", context)


@login_required
def change_username(request):
    username = Author.objects.get(user = request.user)
    
    if request.method == "POST":
        new_username = request.POST.get('new_username')
        username.username = new_username
        username.save()
        
    return redirect(reverse("panel"))


