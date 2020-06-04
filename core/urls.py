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
from auth_user.views import message_delete, message_write, message_read, messages, user_create, change_tag_color, login_view, logout_view, user_view, user_gallery_view, change_username, user_news_view
from gallery.views import add_mult_image, add_mult_file, gallery_view, gallery_create, gallery_delete, gallery_update, one_gallery, add_image, send_form_ajax, images_view, image_delete, add_file, send_form_ajax_file, file_view, file_delete
from webs.views import esport, abso, course, contact, web_create, web_delete, web_edit, web_view, webs, webs_cat_create, webs_cat_edit,webs_cat_delete,web_cat_view
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('nowosci/', news, name="news"),
    path('kontakt/', contact, name="contact"),
    path('kursy/', course, name="course"),
    path('absolwenci/', abso, name="abso"),
    path('esport/', esport, name="esport"),
    
    
    path('nowosci/<slug>/', post, name="post"),
    path('panel/nowosci/<slug>/update/', post_update, name="post-update"),
    path('panel/nowosci/<slug>/main-update/', post_main_update, name="main-post-update"),
    path('panel/nowosci/<slug>/delete/', post_delete, name="post-delete"),
    path('panel/news/create/', post_create, name="post-create"),
    
    path('panel/change_color/', change_tag_color, name="change_tag_color"),
    path('panel/user_create/', user_create, name="user_create"),
    path('panel/messages/', messages, name="messages"),
    path('panel/messages/<slug>/read/', message_read, name="message_read"),
    path('panel/messages/<slug>/write/', message_write, name="message_write"),
    path('panel/messages/<slug>/delete/', message_delete, name="message_delete"),
    
    
    path('panel/<slug>/wstrzymaj/', post_freez, name="post-freez"),
    path('tinymce/', include('tinymce.urls')),
    path('logowanie/', login_view, name="login"),
    path('wylogowanie/', logout_view, name="logout"),
    
    path('panel/', user_view, name="panel"),
    path('panel/nowosci/', user_news_view, name="panel-news"),
    
    path('panel/galeria/', user_gallery_view, name="panel-gallery"),
    
    path('panel/add_image/', add_image, name="add_image"),
    path('panel/add_image/ajax/', send_form_ajax, name="send_form_ajax"),
    path('panel/add_mult_image/ajax', add_mult_image, name="add_mult_image"),
    path('panel/images/', images_view, name="panel-images"),
    path('panel/images/<slug>/delete/', image_delete, name="image_delete"),
    
    path('panel/add_file/', add_file, name="add_file"),
    path('panel/add_file/ajax', send_form_ajax_file, name="send_form_ajax_file"),
    path('panel/add_mult_file/ajax/', add_mult_file, name="add_mult_file"),
    path('panel/file/', file_view, name="panel-file"),
    path('panel/file/<slug>/delete/', file_delete, name="file_delete"),
    
    path('panel/web/create/', web_create, name="web_create"),
    path('panel/web/<slug>/delete/', web_delete, name="web_delete"),
    path('panel/web/<slug>/edit/', web_edit, name="web_edit"),
    path('panel/web/', web_view, name="web_view"),
    path('strona/<slug>/', webs, name="webs"),
    
    
    path('panel/web_cat/create/', webs_cat_create, name="webs_cat_create"),
    path('panel/web_cat/<slug>/edit/', webs_cat_edit, name="webs_cat_edit"),
    path('panel/web_cat/<slug>/delete/', webs_cat_delete, name="webs_cat_delete"),
    path('panel/web_cat/', web_cat_view, name="web_cat_view"),
    
    path('galeria/', gallery_view, name="gallery"),
    
    path('galeria/<slug>/', one_gallery , name="galeria_one"),
    path('gallery/create/', gallery_create, name="galeria-create"),
    path('galeria/<slug>/delete/', gallery_delete, name="galeria-delete"),
    path('galeria/<slug>/update/', gallery_update, name="galeria-update"),
    
    path('panel/zmien_nazwe/', change_username, name="change_username"),
    
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

handler404 = 'webs.views.error_404_view'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
