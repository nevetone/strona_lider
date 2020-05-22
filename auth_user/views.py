from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse
from .forms import LoginForm, RegistrationForm
from news.models import Author, News, MainNews, Files, Webs, Pictures, Gallery
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.models import User
from .models import Rangs
# Create your views here.

def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

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
    
    user = get_author(request.user)
    if user.rank.create_new:
        pass
    else:
        raise Http404
    
        
    context={'news':qs, 'mainnews':qs2 }
    return render(request, "panel.html", context)

@login_required
def user_view(request):
    autor = Author.objects.get(user = request.user)
    if autor.username:
        username = autor.username
    else:
        username = autor.user.username
    
    
    context={'username':username,'autor':autor,}
    return render(request, "main-panel.html", context)


@login_required
def user_gallery_view(request):
    qs = Gallery.objects.order_by('-timestamp')
    
    user = get_author(request.user)
    if user.rank.create_gallery:
        pass
    else:
        raise Http404
    
        
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



@login_required
def change_tag_color(request):
    autor = Author.objects.get(user = request.user)
    text_color = request.POST.get('cat_text_color')
    tag_color = request.POST.get('tag_color')
    
    autor.cat_color = tag_color
    autor.cat_text_color = text_color
    autor.save()
    
    
    return redirect(reverse("panel"))


@login_required
def user_create(request):
    user = get_author(request.user)
    if user.rank.create_user:
        pass
    else:
        raise Http404
    
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.save()
        newUser = User.objects.get(username = form.instance.username)
        new_autor = Author(user = newUser, rank = Rangs.objects.get(name="User"))
        new_autor.save()
        return redirect(reverse("panel"))

    context={
        'form':form,
    }
    return render(request, "register.html", context)
