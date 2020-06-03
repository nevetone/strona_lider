from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse
from .forms import LoginForm, RegistrationForm
from news.models import WebCategory, Category, Author, News, MainNews, Files, Webs, Pictures, Gallery
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
    all_webs = WebCategory.objects.all()
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect('/panel/')
    else:
        pass
    
    context={"form":form,'all_webs':all_webs,}
    return render(request, "login.html", context)



@login_required
def user_news_view(request):
    all_webs = WebCategory.objects.all()
    qs = News.objects.order_by('-timestamp')
    qs2 = MainNews.objects.all()
    qs3 = []
    
    user = get_author(request.user)
    if user.rank.create_new:
        pass
    else:
        raise Http404
    
    if request.method == "POST":
        news_name = request.POST.get('news_name')
        user_cat = request.POST.get('user_cat')
        
        if user_cat and user_cat != "" and news_name:
            aut = User.objects.get(username = user_cat)
            aut2 = Author.objects.get(user = aut)
            qs = News.objects.filter(author = aut2).filter(title__icontains = news_name).order_by('-timestamp')
        elif user_cat and user_cat != "" and not news_name:
            aut = User.objects.get(username = user_cat)
            aut2 = Author.objects.get(user = aut)
            qs = News.objects.filter(author = aut2).order_by('-timestamp')
        elif news_name and not user_cat and user_cat == "" :
            qs = News.objects.filter(title__icontains = news_name).order_by('-timestamp')
        else:
            qs = News.objects.order_by('-timestamp')
    
    for item in qs:
        if item.author.username == user.username or item.author.username == user.user.username:
            qs3.append(item)
    
    if user.rank.create_user == True:
        qs3 = qs
    
    all_users = Author.objects.all()
    all_cat = Category.objects.all()
    
    context={'news':qs3, 'mainnews':qs2,'all_webs':all_webs, 'user1':user, 'all_users':all_users, 'all_cat':all_cat }
    return render(request, "panel.html", context)

@login_required
def user_view(request):
    all_webs = WebCategory.objects.all()
    autor = Author.objects.get(user = request.user)
    if autor.username:
        username = autor.username
    else:
        username = autor.user.username
    
    
    context={'username':username,'autor':autor,'all_webs':all_webs,}
    return render(request, "main-panel.html", context)


@login_required
def user_gallery_view(request):
    all_webs = WebCategory.objects.all()
    qs = Gallery.objects.order_by('-timestamp')
    
    user = get_author(request.user)
    if user.rank.create_gallery:
        pass
    else:
        raise Http404
    
        
    context={'gallery':qs,'all_webs':all_webs, }
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
    all_webs = WebCategory.objects.all()
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
        'form':form,'all_webs':all_webs,
    }
    return render(request, "register.html", context)
