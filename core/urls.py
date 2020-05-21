"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from news.views import index, news, post, post_update, post_delete, post_create, post_freez, post_main_update
from django.conf import settings
from django.conf.urls.static import static
from auth_user.views import login_view, logout_view, user_view, user_gallery_view, change_username, user_news_view
from gallery.views import gallery_view, gallery_create, gallery_delete, gallery_update, one_gallery, add_image, send_form_ajax, images_view, image_delete, add_file, send_form_ajax_file, file_view, file_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('nowosci/', news, name="news"),
    
    path('nowosci/<slug>/', post, name="post"),
    path('nowosci/<slug>/update/', post_update, name="post-update"),
    path('nowosci/<slug>/main-update/', post_main_update, name="main-post-update"),
    path('nowosci/<slug>/delete/', post_delete, name="post-delete"),
    path('news/create/', post_create, name="post-create"),
    
    

    
    
    path('panel/<slug>/wstrzymaj/', post_freez, name="post-freez"),
    path('tinymce/', include('tinymce.urls')),
    path('logowanie/', login_view, name="login"),
    path('wylogowanie/', logout_view, name="logout"),
    path('panel/', user_view, name="panel"),
    path('panel/nowosci/', user_news_view, name="panel-news"),
    
    path('panel/galeria/', user_gallery_view, name="panel-gallery"),
    
    path('panel/add_image/', add_image, name="add_image"),
    path('panel/add_image/ajax', send_form_ajax, name="send_form_ajax"),
    path('panel/images/', images_view, name="panel-images"),
    path('panel/images/<slug>/delete/', image_delete, name="image_delete"),
    
    path('panel/add_file/', add_file, name="add_file"),
    path('panel/add_file/ajax', send_form_ajax_file, name="send_form_ajax_file"),
    path('panel/file/', file_view, name="panel-file"),
    path('panel/file/<slug>/delete/', file_delete, name="file_delete"),
    
    
    
    path('galeria/', gallery_view, name="gallery"),
    
    
    
    path('galeria/<slug>/', one_gallery , name="galeria_one"),
    path('gallery/create/', gallery_create, name="galeria-create"),
    path('galeria/<slug>/delete/', gallery_delete, name="galeria-delete"),
    path('galeria/<slug>/update/', gallery_update, name="galeria-update"),
    
    path('panel/zmien_nazwe', change_username, name="change_username"),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)