from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse
from news.models import Webs, Author, WebCategory
from .forms import WebCreateForm, WebCatCreateForm
from django.http import JsonResponse
from auth_user.models import Messages
from django.core.mail import send_mail

# Create your views here.

def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

@login_required
def web_create(request):
    all_webs = WebCategory.objects.all()
    template="web_create.html"
    form = WebCreateForm(request.POST or None, request.FILES or None)
    title = "Stwórz Podstronę"
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = get_author(request.user)
            form.save()
            
            return redirect(reverse("webs", kwargs={
                'slug': form.instance.web_name
            }))
    
    user = get_author(request.user)
    if user.rank.create_webs:
        pass
    else:
        raise Http404
    
    context = {
        'form':form, 'title':title,'all_webs':all_webs,
    }
    return render(request, template, context)

@login_required
def web_edit(request, slug):
    all_webs = WebCategory.objects.all()
    template="web_create.html"
    web = get_object_or_404(Webs, web_name=slug)
    form = WebCreateForm(request.POST or None, request.FILES or None, instance=web)
    title = "Edytuj Podstronę"
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = get_author(request.user)
            form.save()
            
            return redirect(reverse("webs", kwargs={
                'slug': form.instance.web_name
            }))
            
    user = get_author(request.user)
    if user.rank.create_webs:
        pass
    else:
        raise Http404
    
    context = {
        'form':form, 'title':title, 'all_webs':all_webs,
    }
    return render(request, template, context)

@login_required
def web_delete(request, slug):
    web = get_object_or_404(Webs, web_name=slug)
    web.delete()
            
    user = get_author(request.user)
    if user.rank.create_webs:
        pass
    else:
        raise Http404
    
    return redirect(reverse("web_view"))

@login_required
def web_view(request):
    all_webs = WebCategory.objects.all()
    template="web-panel.html"
    webs = Webs.objects.order_by('-timestamp')
            
    user = get_author(request.user)
    if user.rank.create_webs:
        pass
    else:
        raise Http404
    
    context = {'webs':webs, 'all_webs':all_webs,}
    return render(request, template, context)

def webs(request, slug):
    all_webs = WebCategory.objects.all()
    template="webs.html"
    web = get_object_or_404(Webs, web_name=slug)
    

    
    context = {'web':web, 'all_webs':all_webs,}
    return render(request, template, context)




@login_required
def webs_cat_create(request):
    all_webs = WebCategory.objects.all()
    template="web_create.html"
    form = WebCatCreateForm(request.POST or None, request.FILES or None)
    title = "Stwórz Kategorię Strony"
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = get_author(request.user)
            form.save()
            
            return redirect(reverse("web_cat_view"))
            
    context = {
        'form':form, 'title':title, 'all_webs':all_webs,
    }
    return render(request, template, context)

@login_required
def webs_cat_edit(request, slug):
    all_webs = WebCategory.objects.all()
    template="web_create.html"
    web = get_object_or_404(WebCategory, web_cat_name=slug)
    form = WebCatCreateForm(request.POST or None, request.FILES or None, instance=web)
    title = "Edytuj Kategorię strony"
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = get_author(request.user)
            form.save()
            
            return redirect(reverse("web_cat_view"))
            
    context = {
        'form':form, 'title':title, 'all_webs':all_webs,
    }
    return render(request, template, context)

@login_required
def webs_cat_delete(request, slug):
    web = get_object_or_404(WebCategory, web_cat_name=slug)
    web.delete()
    return redirect(reverse("web_cat_view"))

@login_required
def web_cat_view(request):
    all_webs = WebCategory.objects.all()
    template="web-cat-panel.html"
    webs = WebCategory.objects.order_by('-timestamp')
    
    context = {'webs':webs, 'all_webs':all_webs,}
    return render(request, template, context)


def validateEmail(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False


def contact(request):
    template="kontakt.html"
    all_webs = WebCategory.objects.all()
    context ={'all_webs':all_webs,}
    
    if request.is_ajax and request.method == "POST":
        nickname = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('title')
        message = request.POST.get('message')
        send_coppy = request.POST.get('send_coppy')
        
        if send_coppy:
            send_coppy = True
        else:
            send_coppy = False
            
        
        if validateEmail(email):
            if nickname and email and title and message:
                messages = Messages(title = title, message = message, sender_nickname=nickname, sender_email=email, send_back=send_coppy)
                messages.save()
                if send_coppy:
                    send_mail(title, message, 'nevetfortests@gmail.com', [email])
                return JsonResponse({'message':'Wiadomość została wysłana, wktótce odpiszemy!'}, status=200)
        else:
            return JsonResponse({'message':'Sprawdź poprawność emaila'}, status=400)
    
    return render(request, template, context)

def course(request):
    template="kursy.html"
    all_webs = WebCategory.objects.all()
    context ={'all_webs':all_webs,}
    return render(request, template, context)


def abso(request):
    template="abso.html"
    all_webs = WebCategory.objects.all()
    
    context ={'all_webs':all_webs,}
    return render(request, template, context)


def esport(request):
    template="esport.html"
    all_webs = WebCategory.objects.all()
    
    context ={'all_webs':all_webs,}
    return render(request, template, context)



def error_404_view(request, exception):
    all_webs = WebCategory.objects.all()
    return render(request,'404.html',{'all_webs':all_webs,})

