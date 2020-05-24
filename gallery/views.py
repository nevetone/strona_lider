from django.shortcuts import get_object_or_404, redirect, render
from news.models import Gallery, Pictures, Files, WebCategory
from django.urls import reverse
from news.forms import GalleryForm, ImagesCount
from django.contrib.auth.decorators import login_required
from news.models import Author
from django.http import JsonResponse
from django.http import Http404

def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None



# Create your views here.
def gallery_view(request):
    all_webs = WebCategory.objects.all()
    template = "gallery.html"
    gallery = Gallery.objects.order_by('-timestamp')
    
    
    context={
        'all_gallery':gallery, 'all_webs':all_webs,
    }
    return render(request, template, context)

# Create your views here.
def one_gallery(request, slug):
    all_webs = WebCategory.objects.all()
    template = "one_gallery.html"
    gallery_images = get_object_or_404(Gallery, gallery_name=slug)
    images = []
    iamges_count = gallery_images.pictures.count()
    
    for image in gallery_images.pictures.all():
        images.append(image)
    
    context={
        'images':images, 'gallery':gallery_images, 'iamges_count':iamges_count, 'all_webs':all_webs,
    }
    return render(request, template, context)



@login_required
def gallery_create(request):
    all_webs = WebCategory.objects.all()
    form = GalleryForm(request.POST or None, request.FILES or None)
    title = "Stwórz Galerię"
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = get_author(request.user)
            form.save()
            gallery = Gallery.objects.get(gallery_name = form.instance.gallery_name )
            for imgs in gallery.pictures.all():
                imgs.has_gallery = True
                imgs.save()
                
            
            return redirect(reverse("gallery"))
            
    user = get_author(request.user)
    if user.rank.create_gallery:
        pass
    else:
        raise Http404
    
    context = {
        'form':form, 'title':title, 'all_webs':all_webs,
    }
    return render(request, "news_create.html", context)


@login_required
def gallery_update(request, slug):
    all_webs = WebCategory.objects.all()
    gallery = get_object_or_404(Gallery, gallery_name=slug)
    form = GalleryForm(request.POST or None,request.FILES or None,instance=gallery)
    title = "Edytuj Galerię"
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = get_author(request.user)
            form.save()
            return redirect(reverse("galeria", kwargs={
                'slug': form.instance.gallery_name
            }))
            
    user = get_author(request.user)
    if user.rank.create_gallery:
        pass
    else:
        raise Http404
    
    context = {
        'form':form, 'title':title, 'all_webs':all_webs,
    }
    return render(request, "news_create.html", context)


@login_required
def gallery_delete(request, slug):
    gallery = get_object_or_404(Gallery, gallery_name=slug)
    gallery.delete()
    
            
    user = get_author(request.user)
    if user.rank.create_gallery:
        pass
    else:
        raise Http404
    
    return redirect(reverse("galeria-delete"))



# images
@login_required
def add_image(request):
    all_webs = WebCategory.objects.all()
    context={'all_webs':all_webs,}
            
    user = get_author(request.user)
    if user.rank.adding_images:
        pass
    else:
        raise Http404
    
    
    return render(request, "add_images.html", context)



@login_required
def send_form_ajax(request):

    if request.is_ajax and request.method == "POST":
        
        clicked = str(request.POST.get('current_clicked'))
        image_name = request.POST.get('image'+clicked+'_name')
        image = request.FILES.get('image'+str(clicked))
        
        save = Pictures(picture_title=image_name, picture=image, author=get_author(request.user))
        save.save()
        if image is not None and image_name is not None:
            return JsonResponse({'clicked':clicked, 'error':'false',}, status=200)

    user = get_author(request.user)
    if user.rank.adding_images:
        pass
    else:
        raise Http404
    
    return redirect(reverse("add_image"))


@login_required
def images_view(request):
    images = Pictures.objects.order_by('-timestamp')
    all_webs = WebCategory.objects.all()
    
    user = get_author(request.user)
    if user.rank.adding_images:
        pass
    else:
        raise Http404
    
    
    context={
        'images':images, 'all_webs':all_webs,
    }
    return render(request, 'images-panel.html', context)

@login_required
def image_delete(request, slug):
    images = get_object_or_404(Pictures, picture=slug)
    images.delete()
    
    user = get_author(request.user)
    if user.rank.adding_images:
        pass
    else:
        raise Http404
    
    
    return redirect(reverse("panel-images"))




# files

@login_required
def add_file(request):
    all_webs = WebCategory.objects.all()
    context={'all_webs':all_webs,}
    
    user = get_author(request.user)
    if user.rank.create_files:
        pass
    else:
        raise Http404
    
    
    return render(request, "add_file.html", context)


@login_required
def send_form_ajax_file(request):

    if request.is_ajax and request.method == "POST":
        
        clicked = str(request.POST.get('current_clicked'))
        file_name = request.POST.get('file'+clicked+'_name')
        file = request.FILES.get('file'+str(clicked))
        
        save = Files(file_name=file_name, file=file, author=get_author(request.user))
        save.save()
        if file is not None and file_name is not None:
            return JsonResponse({'clicked':clicked, 'error':'false',}, status=200)
    
    user = get_author(request.user)
    if user.rank.create_files:
        pass
    else:
        raise Http404
    
    return redirect(reverse("add_file"))


@login_required
def file_view(request):
    files = Files.objects.order_by('-timestamp')
    all_webs = WebCategory.objects.all()
    
    user = get_author(request.user)
    if user.rank.create_files:
        pass
    else:
        raise Http404
    
    context={
        'files':files, 'all_webs':all_webs,
    }
    return render(request, 'file-panel.html', context)

@login_required
def file_delete(request, slug):
    files = get_object_or_404(Files, file=slug)
    files.delete()
    
    
    user = get_author(request.user)
    if user.rank.create_files:
        pass
    else:
        raise Http404
    
    
    return redirect(reverse("panel-file"))