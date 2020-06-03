from django.shortcuts import get_object_or_404, redirect, render
from news.models import Gallery, Pictures, Files, WebCategory, Category
from django.urls import reverse
from news.forms import GalleryForm, ImagesCount, EditGalleryForm
from django.contrib.auth.decorators import login_required
from news.models import Author
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import Http404
import os
from django.core.files.base import ContentFile
from django.utils import timezone
from django.utils.crypto import get_random_string


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
                imgs.images_in = form.instance.gallery_name
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
    user = get_author(request.user)
    if user.rank.create_gallery:
        pass
    else:
        raise Http404
    all_webs = WebCategory.objects.all()
    gallery = get_object_or_404(Gallery, gallery_name=slug)
    
    if gallery.author.user != request.user:
        if user.rank.create_user == True:
            pass
        else:
            raise Http404
    else:
        pass
    
    form = EditGalleryForm(request.POST or None,request.FILES or None,instance=gallery)
    title = "Edytuj Galerię"
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = get_author(request.user)
            gallery = Gallery.objects.get(gallery_name = form.instance.gallery_name )
            gallery_images = gallery.pictures.all()
            form.save()
            for imgs in gallery.pictures.all():
                imgs.has_gallery = True
                imgs.images_in = form.instance.gallery_name
                imgs.save()
                
            return redirect(reverse("galeria_one", kwargs={
                'slug': form.instance.gallery_name
            }))
    context = {
        'form':form, 'title':title, 'all_webs':all_webs,
    }
    return render(request, "news_create.html", context)


@login_required
def gallery_delete(request, slug):
    user = get_author(request.user)
    if user.rank.create_gallery:
        pass
    else:
        raise Http404
    
    gallery = get_object_or_404(Gallery, gallery_name=slug)
    
    if gallery.author.user != request.user:
        if user.rank.create_user == True:
            for x in gallery.pictures.all():
                x.images_in = ""
                x.has_gallery = False
                x.save()
            gallery.delete()
        else:
            raise Http404
    else:
        if user.rank.create_user == True:
            for x in gallery.pictures.all():
                x.images_in = ""
                x.has_gallery = False
                x.save()
            gallery.delete()
    return redirect(reverse("panel-gallery"))



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
    user = get_author(request.user)
    if user.rank.adding_images:
        pass
    else:
        raise Http404
    user = get_author(request.user)
    if request.is_ajax and request.method == "POST":
        
        clicked = str(request.POST.get('current_clicked'))
        image_name = request.POST.get('image'+clicked+'_name')
        image = request.FILES.get('image'+str(clicked))
        folder = 'wszystkie_pliki/zdjecia/'+str(timezone.now().year)+'/'
        BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        try:
            os.mkdir(os.path.join(BASE_PATH, folder))
        except:
            pass
        
        try:
            os.mkdir(os.path.join(BASE_PATH, folder, image_name))
        except:
            pass
        
        name, extension = os.path.splitext(image.name)
        currentYear = timezone.now().year
        uploaded_filename = image_name+'_'+str(clicked)+'_'+str(currentYear)+'_'+get_random_string(length=10)+extension
        full_filename = os.path.join(BASE_PATH, folder, image_name, uploaded_filename)
        fout = open(full_filename, 'wb+')
        file_content = ContentFile( image.read() )
        for chunk in file_content.chunks():
            fout.write(chunk)
        fout.close()
        
        save = Pictures(picture_title=image_name, picture=image, author=get_author(request.user))
        save.save()
        if image is not None and image_name is not None:
            return JsonResponse({'clicked':clicked, 'error':'false',}, status=200)

    return redirect(reverse("add_image"))


@login_required
def images_view(request):
    qs = Pictures.objects.order_by('-timestamp')
    all_webs = WebCategory.objects.all()
    qs3 = []
    
    user = get_author(request.user)
    if user.rank.adding_images:
        pass
    else:
        raise Http404
    
    
    if request.method == "POST":
        image_name = request.POST.get('image_name')
        user_cat = request.POST.get('user_cat')

        
        if user_cat and user_cat != "" and image_name:
            aut = User.objects.get(username = user_cat)
            aut2 = Author.objects.get(user = aut)
            qs = Pictures.objects.filter(author = aut2).filter(picture_title__icontains = image_name).order_by('-timestamp')
        elif user_cat and user_cat != "" and not image_name:
            aut = User.objects.get(username = user_cat)
            aut2 = Author.objects.get(user = aut)
            qs = Pictures.objects.filter(author = aut2).order_by('-timestamp')
        elif image_name and not user_cat and user_cat == "" :
            qs = Pictures.objects.filter(picture_title__icontains = image_name).order_by('-timestamp')
        else:
            qs = Pictures.objects.order_by('-timestamp')
    
    for item in qs:
        if item.author.username == user.username or item.author.username == user.user.username:
            qs3.append(item)
    
    if user.rank.create_user == True:
        qs3 = qs
    
    all_users = Author.objects.all()
    all_cat = Category.objects.all()
    
    
    context={
        'images':qs3, 'all_webs':all_webs,'user1':user, 'all_users':all_users, 'all_cat':all_cat
    }
    return render(request, 'images-panel.html', context)

@login_required
def image_delete(request, slug):
    user = get_author(request.user)
    if user.rank.adding_images:
        pass
    else:
        raise Http404
    images = get_object_or_404(Pictures, picture=slug)
    
    if images.author.user != request.user:
        if user.rank.create_user == True:
            images.delete()
        else:
            raise Http404
    else:
        images.delete()
    
    return redirect(reverse("panel-images"))




# files

@login_required
def add_file(request):
    user = get_author(request.user)
    if user.rank.create_files:
        pass
    else:
        raise Http404
    
    all_webs = WebCategory.objects.all()
    context={'all_webs':all_webs,}
    

    
    
    return render(request, "add_file.html", context)


@login_required
def send_form_ajax_file(request):

    if request.is_ajax and request.method == "POST":
        
        clicked = str(request.POST.get('current_clicked'))
        file_name = request.POST.get('file'+clicked+'_name')
        file = request.FILES.get('file'+str(clicked))
        
        folder = 'wszystkie_pliki/pliki/'+str(timezone.now().year)+'/'
        BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        try:
            os.mkdir(os.path.join(BASE_PATH, folder))
        except:
            pass
        
        try:
            os.mkdir(os.path.join(BASE_PATH, folder, file_name))
        except:
            pass
        
        name, extension = os.path.splitext(file.name)
        currentYear = timezone.now().year
        uploaded_filename = file_name+'_'+str(clicked)+'_'+str(currentYear)+'_'+get_random_string(length=10)+extension
        full_filename = os.path.join(BASE_PATH, folder ,file_name, uploaded_filename)
        fout = open(full_filename, 'wb+')
        file_content = ContentFile( file.read() )
        for chunk in file_content.chunks():
            fout.write(chunk)
        fout.close()
        
        
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
    qs = Files.objects.order_by('-timestamp')
    all_webs = WebCategory.objects.all()
    qs3 = []
    
    user = get_author(request.user)
    if user.rank.create_files:
        pass
    else:
        raise Http404
    
    
    
    if request.method == "POST":
        file_name = request.POST.get('file_name')
        user_cat = request.POST.get('user_cat')

        
        if user_cat and user_cat != "" and file_name:
            aut = User.objects.get(username = user_cat)
            aut2 = Author.objects.get(user = aut)
            qs = Files.objects.filter(author = aut2).filter(file_name__icontains = file_name).order_by('-timestamp')
        elif user_cat and user_cat != "" and not file_name:
            aut = User.objects.get(username = user_cat)
            aut2 = Author.objects.get(user = aut)
            qs = Files.objects.filter(author = aut2).order_by('-timestamp')
        elif file_name and not user_cat and user_cat == "" :
            qs = Files.objects.filter(file_name__icontains = file_name).order_by('-timestamp')
        else:
            qs = Files.objects.order_by('-timestamp')
    
    for item in qs:
        if item.author.username == user.username or item.author.username == user.user.username:
            qs3.append(item)
    
    if user.rank.create_user == True:
        qs3 = qs
    
    all_users = Author.objects.all()
    all_cat = Category.objects.all()
    
    context={
        'files':qs3, 'all_webs':all_webs,'user1':user, 'all_users':all_users, 'all_cat':all_cat
    }
    return render(request, 'file-panel.html', context)

@login_required
def file_delete(request, slug):
    user = get_author(request.user)
    if user.rank.create_files:
        pass
    else:
        raise Http404
    files = get_object_or_404(Files, file=slug)
    
    if files.author.user != request.user:
        if user.rank.create_user == True:
            files.delete()
        else:
            raise Http404
    else:
        files.delete()
    
    return redirect(reverse("panel-file"))


@login_required
def add_mult_image(request):
    user = get_author(request.user)
    if user.rank.adding_images:
        pass
    else:
        raise Http404
    
    folder = 'wszystkie_pliki/zdjecia/'+str(timezone.now().year)+'/'
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    try:
        os.mkdir(os.path.join(BASE_PATH, folder))
    except:
        pass
    
    if request.is_ajax and request.method == "POST":
        images_name = request.POST.get('images_name')
        try:
            os.mkdir(os.path.join(BASE_PATH, folder, images_name))
        except:
            pass
        pomocnicza = 0
        for f in request.FILES.getlist('images_mult'):
            
            name, extension = os.path.splitext(f.name)
            currentYear = timezone.now().year
            uploaded_filename = images_name+'_'+str(pomocnicza)+'_'+str(currentYear)+'_'+get_random_string(length=10)+extension
            full_filename = os.path.join(BASE_PATH, folder, images_name, uploaded_filename)
            fout = open(full_filename, 'wb+')
            file_content = ContentFile( f.read() )
            for chunk in file_content.chunks():
                fout.write(chunk)
            fout.close()
            pomocnicza = pomocnicza + 1
 
            images = Pictures(picture_title = images_name, picture=f, author = user)
            images.save()
            
    return JsonResponse({'error':'false'}, status=200)
        
    return redirect(reverse("add_image"))

@login_required
def add_mult_file(request):
    user = get_author(request.user)
    if user.rank.create_files:
        pass
    else:
        raise Http404
    
    folder = 'wszystkie_pliki/pliki/'+str(timezone.now().year)+'/'
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    try:
        os.mkdir(os.path.join(BASE_PATH, folder))
    except:
        pass
    
    if request.is_ajax and request.method == "POST":
        files_name = request.POST.get('files_name')
        try:
            os.mkdir(os.path.join(BASE_PATH, folder, files_name))
        except:
            pass
        pomocnicza = 0
        for f in request.FILES.getlist('files_mult'):
            
            name, extension = os.path.splitext(f.name)
            currentYear = timezone.now().year
            uploaded_filename = files_name+'_'+str(pomocnicza)+'_'+str(currentYear)+'_'+get_random_string(length=10)+extension
            full_filename = os.path.join(BASE_PATH, folder, files_name, uploaded_filename)
            fout = open(full_filename, 'wb+')
            file_content = ContentFile( f.read() )
            for chunk in file_content.chunks():
                fout.write(chunk)
            fout.close()
            pomocnicza = pomocnicza + 1
            
            files = Files(file_name = files_name, file=f, author = user)
            files.save()
            
    return JsonResponse({'error':'false'}, status=200)
        
    return redirect(reverse("add_file"))