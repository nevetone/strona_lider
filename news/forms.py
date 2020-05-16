from tinymce import TinyMCE
from django import forms
from .models import News, MainNews, Category, Gallery

class TinyMCEWidget(TinyMCE):
    def use_required_atribute(self, *args):
        return False

class NewsForm(forms.ModelForm):

    content = forms.CharField(widget=TinyMCE(attrs={'cols': 30, 'rows': 10}), required=False, label="Text na podstronie")
    title = forms.CharField(required = True, label='Tytuł')
    overview = forms.CharField(required = True, label='Wiadomość')
    has_thumbnail = forms.BooleanField(required = False, label='Czy posiada zdjęcie główne')
    thumbnail = forms.ImageField(required = False, label='Zdjęcie główne ( jeżeli posiada zdjęcie )')
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required = True, label='Kategoria')
    web_name = forms.CharField(required = True, label='Nazwa Strony')
    has_own_web = forms.BooleanField(required = False, label='Czy posiada podstronę')
    has_gallery = forms.BooleanField(required = False, label='Czy posiada galerię')
    gallery = forms.ModelMultipleChoiceField(queryset=Gallery.objects.all(), required = False, label='Wybierz galerię ( jeżeli posiada galerię )')
    
    
    
    class Meta:
        model = News
        fields = ('title', 'overview','has_thumbnail','thumbnail', 'category','web_name', 'has_own_web','content','has_gallery','gallery',)


class MainNewsForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 30, 'rows': 10}), required=False, label="Podstrona")
    
    class Meta:
        model = MainNews
        fields = ('title', 'overview','thumbnail', 'category','web_name', 'has_own_web','content','has_gallery','gallery',)