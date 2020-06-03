from django.shortcuts import get_object_or_404, redirect, render
from .models import News, MainNews, Author, WebCategory, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import NewsForm, MainNewsForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import Http404


def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


# Create your views here.
def index(request):
    template = 'index.html'
    queryset1 = News.objects.order_by('-timestamp')
    queryset2 = MainNews.objects.filter(featured=True)
    page_request_var = 'page'
    paginator = Paginator(queryset1, 6)
    page = request.GET.get(page_request_var)
    
    try:
        paginated_querrysey = paginator.page(page)
    except PageNotAnInteger:
        paginated_querrysey = paginator.page(1)
    except EmptyPage:
        paginated_querrysey = paginator.page(paginator.num_pages)
        
    all_webs = WebCategory.objects.all()
    
    
    context={
        'queryset1':paginated_querrysey,
        'queryset2':queryset2,
        'page_request_var':page_request_var,
        'all_webs':all_webs,
        
    }
    return render(request, template, context)


def get_cat(cat):
    for category in Category.objects.all():
        if category.title == cat:
            return category

def news(request):
    template = 'news.html'
    categ = Category.objects.all()
    queryset1 = News.objects.order_by('-timestamp')
    
    if request.method == "POST":
        cat = request.POST.get('category')
        title = request.POST.get('title')
        
        if cat and title == "":
            queryset1 = News.objects.filter(category=get_cat(cat)).order_by('-timestamp')
        elif title and cat == "":
            queryset1 = News.objects.filter(title__icontains = title).order_by('-timestamp')
        elif title and cat:
            queryset1 = News.objects.filter(title__icontains = title).filter(category=get_cat(cat)).order_by('-timestamp')
        else:
            queryset1 = News.objects.order_by('-timestamp')
        
    
    if not queryset1:
        message = "Brak wyników"
    else:
        message = None
    
    
    queryset2 = MainNews.objects.filter(featured=True)
    all_webs = WebCategory.objects.all()
    context={'queryset1':queryset1, 'queryset2':queryset2,'all_webs':all_webs,'categ':categ,'message':message}
    return render(request, template, context)

def post(request, slug):
    template = 'one.html'
    
    all_webs = WebCategory.objects.all()
    try:
        post = News.objects.get(web_name=slug)
    except:
        post = None
        main_post = True
    try:
        mainpost = MainNews.objects.get(web_name=slug)
    except:
        mainpost = None
        main_post = False

    if post:
        content = post
    elif mainpost:
        if mainpost.has_own_web is False:
            raise Http404
        else:
            content = mainpost
    else:
        raise Http404

    print(main_post)
    context={
         'main_post':main_post, 'post':content,'all_webs':all_webs,
    }
    return render(request, template, context)

@login_required
def post_create(request):
    all_webs = WebCategory.objects.all()
    form = NewsForm(request.POST or None, request.FILES or None)
    title = "Stwórz Post"
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = get_author(request.user)
            form.save()
            if not form.instance.has_own_web:
                return redirect(reverse("panel"))
            
            return redirect(reverse("post", kwargs={
                'slug': form.instance.web_name
            }))
            
    user = get_author(request.user)
    if user.rank.create_new:
        pass
    else:
        raise Http404
    
    context = {
        'form':form, 'title':title,'all_webs':all_webs,
    }
    return render(request, "news_create.html", context)

@login_required
def post_update(request, slug):
    user = get_author(request.user)
    
    if user.rank.create_new:
        pass
    else:
        raise Http404
    all_webs = WebCategory.objects.all()
    post = get_object_or_404(News, web_name=slug)
    
    
    if post.author.user != request.user:
        if user.rank.create_user == True:
            pass
        else:
            raise Http404
    
    form = NewsForm(request.POST or None,request.FILES or None,instance=post)
    title = "Edytuj Post"
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = get_author(request.user)
            form.save()
            return redirect(reverse("post", kwargs={
                'slug': form.instance.web_name
            }))
            

    
    context = {
        'form':form, 'title':title,'all_webs':all_webs,
    }
    return render(request, "news_create.html", context)

@login_required
def post_delete(request, slug):
    user = get_author(request.user)
    if user.rank.create_new:
        pass
    else:
        raise Http404
    
    post = get_object_or_404(News, web_name=slug)
    if post.author.user != request.user:
        if user.rank.create_user == True:
            post.delete()
            return redirect(reverse("panel-news"))
        raise Http404
    else:
        post.delete()


    
    
    return redirect(reverse("panel-news"))

@login_required
def post_freez(request, slug):
    user = get_author(request.user)
    if user.rank.create_new and user.rank.create_user == True:
        pass
    else:
        raise Http404
    
    post = get_object_or_404(MainNews, web_name=slug)
    post.featured = False
    post.has_own_web = False
    post.save()
    
            

    
    
    return redirect(reverse("panel"))

@login_required
def post_main_update(request, slug):
    user = get_author(request.user)
    if user.rank.create_new and user.rank.create_user == True:
        pass
    else:
        raise Http404
    
    all_webs = WebCategory.objects.all()
    post2 = get_object_or_404(MainNews, web_name=slug)
    form2 = MainNewsForm(request.POST or None,request.FILES or None,instance=post2)
    title = "Edytuj Główny Post"
    if request.method == "POST":
        if form2.is_valid():
            form2.instance.author = get_author(request.user)
            form2.save()
            if form2.instance.has_own_web is False:
                return redirect(reverse("panel"))
            
            return redirect(reverse("post", kwargs={
                'slug': form2.instance.web_name
            }))
            

    
    context = {
        'form':form2, 'title':title, 'all_webs':all_webs,
    }
    return render(request, "news_create.html", context)


