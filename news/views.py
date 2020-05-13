from django.shortcuts import get_object_or_404, redirect, render
from .models import News, MainNews, Author
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import NewsForm, MainNewsForm
from django.urls import reverse


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
    
    post = get_object_or_404(News, web_name=slug)
    
    context={
        'post':post,
    }
    return render(request, template, context)

def post_create(request):
    form = NewsForm(request.POST or None, request.FILES or None)
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
        'form':form
    }
    return render(request, "news_create.html", context)

def post_update(request, slug):
    post = get_object_or_404(News, web_name=slug)
    form = NewsForm(request.POST or None,request.FILES or None,instance=post)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = get_author(request.user)
            form.save()
            return redirect(reverse("post", kwargs={
                'slug': form.instance.web_name
            }))
            
    context = {
        'form':form
    }
    return render(request, "news_create.html", context)

def post_delete(request, slug):
    if request.user.is_authenticated:
        post = get_object_or_404(News, web_name=slug)
        post.delete()
    return redirect(reverse("index"))