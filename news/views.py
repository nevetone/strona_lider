from django.shortcuts import render, get_object_or_404
from .models import News, MainNews
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    template = 'index.html'
    queryset1 = News.objects.all()
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
    queryset1 = News.objects.all()
    context={'queryset1':queryset1}
    return render(request, template, context)

def post(request, slug):
    template = 'one.html'
    
    post = get_object_or_404(News, id=slug)
    
    context={
        'post':post,
    }
    return render(request, template, context)