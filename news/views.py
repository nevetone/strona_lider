from django.shortcuts import get_object_or_404, redirect, render
from .models import News, MainNews, Author
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
        
    
    
    context={
        'queryset1':paginated_querrysey,
        'queryset2':queryset2,
        'page_request_var':page_request_var,
        
    }
    return render(request, template, context)

def news(request):
    template = 'news.html'
    queryset1 = News.objects.order_by('-timestamp')
    queryset2 = MainNews.objects.filter(featured=True)
    context={'queryset1':queryset1, 'queryset2':queryset2,}
    return render(request, template, context)

def post(request, slug):
    template = 'one.html'
    
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
         'main_post':main_post, 'post':content,
    }
    return render(request, template, context)

@login_required
def post_create(request):
    form = NewsForm(request.POST or None, request.FILES or None)
    title = "Stwórz Post"
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = get_author(request.user)
            form.save()
            if not form.instance.has_own_web:
                return redirect(reverse("index"))
            
            return redirect(reverse("post", kwargs={
                'slug': form.instance.web_name
            }))
            
    context = {
        'form':form, 'title':title
    }
    return render(request, "news_create.html", context)

@login_required
def post_update(request, slug):
    post = get_object_or_404(News, web_name=slug)
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
        'form':form, 'title':title
    }
    return render(request, "news_create.html", context)

@login_required
def post_delete(request, slug):
    post = get_object_or_404(News, web_name=slug)
    post.delete()
    return redirect(reverse("index"))

@login_required
def post_freez(request, slug):
    post = get_object_or_404(MainNews, web_name=slug)
    post.featured = False
    post.has_own_web = False
    post.save()
    return redirect(reverse("index"))

@login_required
def post_main_update(request, slug):
    post2 = get_object_or_404(MainNews, web_name=slug)
    form2 = MainNewsForm(request.POST or None,request.FILES or None,instance=post2)
    title = "Edytuj Główny Post"
    if request.method == "POST":
        if form2.is_valid():
            form2.instance.author = get_author(request.user)
            form2.save()
            if form2.instance.has_own_web is False:
                return redirect(reverse("index"))
            
            return redirect(reverse("post", kwargs={
                'slug': form2.instance.web_name
            }))
    context = {
        'form':form2, 'title':title
    }
    return render(request, "news_create.html", context)