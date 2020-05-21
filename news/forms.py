from tinymce import TinyMCE
from django import forms
from .models import News, MainNews, Category, Gallery, Pictures




class TinyMCEWidget(TinyMCE):
    def use_required_atribute(self, *args):
        return False

class NewsForm(forms.ModelForm):

    content = forms.CharField(widget=TinyMCE(attrs={'cols': 30, 'rows': 10}), required=False, label="Text na podstronie")
    title = forms.CharField(required = True, label='Tytuł')
    overview = forms.CharField(required = True, label='Wiadomość')
    has_thumbnail = forms.BooleanField(required = False, label='Czy posiada zdjęcie główne')
    thumbnail = forms.ImageField(required = False, label='Zdjęcie główne ( jeżeli posiada zdjęcie )')
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required = True, label='Wybierz Kategorię ( z L-Shift / L-Ctrl wybierasz kilka )')
    web_name = forms.CharField(required = True, label='Nazwa Strony')
    has_own_web = forms.BooleanField(required = False, label='Czy posiada podstronę')
    has_gallery = forms.BooleanField(required = False, label='Czy posiada galerię')
    gallery = forms.ModelChoiceField(queryset=Gallery.objects.all(), required = False, label='Wybierz galerię ( jeżeli posiada galerię )')

    
    class Meta:
        model = News
        fields = ('title', 'overview','has_thumbnail','thumbnail', 'category','web_name', 'has_own_web','content','has_gallery','gallery',)


class MainNewsForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 30, 'rows': 10}), required=False, label="Text na podstronie")
    title = forms.CharField(required = True, label='Tytuł')
    overview = forms.CharField(required = True, label='Wiadomość')
    has_thumbnail = forms.BooleanField(required = False, label='Czy posiada zdjęcie główne')
    thumbnail = forms.ImageField(required = False, label='Zdjęcie główne ( jeżeli posiada zdjęcie )')
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required = True, label='Wybierz Kategorię ( z L-Shift / L-Ctrl wybierasz kilka )')
    has_own_web = forms.BooleanField(required = False, label='Czy posiada podstronę')
    has_gallery = forms.BooleanField(required = False, label='Czy posiada galerię')
    gallery = forms.ModelChoiceField(queryset=Gallery.objects.all(), required = False, label='Wybierz galerię ( jeżeli posiada galerię )')
    featured = forms.BooleanField(required = False, label='Pokaż na głównej stronie')
    
    
    class Meta:
        model = MainNews
        fields = ('featured', 'title', 'overview','has_thumbnail', 'thumbnail', 'category', 'has_own_web','content','has_gallery','gallery',)



class GalleryForm(forms.ModelForm):
    gallery_name = forms.CharField(required = True, label='Nazwa Galerii')
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required = True, label='Wybierz Kategorię ( z L-Shift / L-Ctrl wybierasz kilka )')
    pictures = forms.ModelMultipleChoiceField(queryset=Pictures.objects.all(), required = True, label='Wybierz Zdjęcia ( z L-Shift / L-Ctrl wybierasz kilka )')
    overview = forms.CharField(required = True, label='Opis Galerii')
    
    class Meta:
        model = Gallery
        fields = ('gallery_name','overview','pictures','category')
        
        
class ImageForm(forms.ModelForm):
    picture_title = forms.CharField(label='Nazwa Zdjęcia')
    picture = forms.ImageField(label='Zdjęcie') 
    to_gallery = forms.BooleanField(label='Czy będzie w Galerii')  
    class Meta:
        model = Pictures
        fields = ('picture_title','picture','to_gallery' )
        
class ImagesCount(forms.Form):
    images_count = forms.IntegerField(label="Ile chcesz wgrać zdjęć")
    class Meta:
        fields=('images_count')