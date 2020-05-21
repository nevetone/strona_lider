from django.shortcuts import get_object_or_404, redirect, render
from news.models import Gallery, Pictures
from django.urls import reverse
from news.forms import GalleryForm, ImagesCount
from django.contrib.auth.decorators import login_required
from news.models import Author
from django.http import JsonResponse

def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None



# Create your views here.
def gallery_view(request):
    template = "gallery.html"
    gallery = Gallery.objects.order_by('-timestamp')
    
    
    context={
        'all_gallery':gallery,
    }
    return render(request, template, context)

# Create your views here.
def one_gallery(request, slug):
    template = "one_gallery.html"
    gallery_images = get_object_or_404(Gallery, gallery_name=slug)
    images = []
    iamges_count = gallery_images.pictures.count()
    
    for image in gallery_images.pictures.all():
        images.append(image)
    
    context={
        'images':images, 'gallery':gallery_images, 'iamges_count':iamges_count
    }
    return render(request, template, context)



@login_required
def gallery_create(request):
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
                
            
            return redirect(reverse("galeria", kwargs={
                'slug': form.instance.gallery_name
            }))
            
    context = {
        'form':form, 'title':title
    }
    return render(request, "news_create.html", context)


@login_required
def gallery_update(request, slug):
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

    context = {
        'form':form, 'title':title
    }
    return render(request, "news_create.html", context)


@login_required
def gallery_delete(request, slug):
    gallery = get_object_or_404(Gallery, gallery_name=slug)
    gallery.delete()
    return redirect(reverse("index"))

images_count = 0
@login_required
def add_image(request):
    global images_count
    if request.is_ajax and request.method == "POST":
        images_count = request.POST.get('images_count')
    context={
        
    }
    return render(request, "add_files.html", context)

@login_required
def send_form_ajax(request):

    

    if request.is_ajax and request.method == "POST":
        context={}
        
        clicked = str(request.POST.get('current_clicked'))
        image_name = request.POST.get('image'+clicked+'_name')
        image = request.FILES.get('image'+str(clicked))
        save = Pictures(picture_title=image_name, picture=image, author=get_author(request.user))
        save.save()
        if image is not None and image_name is not None:
            return JsonResponse({'clicked':clicked,}, status=200)
        else:
            return render(request, "add_files.html", context)
    else:
        return render(request, "add_files.html", context)

    return render(request, "add_files.html", context)