from django import forms
from tinymce import TinyMCE
from news.models import Webs, Pictures, Files, WebCategory

class TinyMCEWidget(TinyMCE):
    def use_required_atribute(self, *args):
        return False

class WebCreateForm(forms.ModelForm):
    web_name = forms.CharField(required=True, label="Nazwa Podstrony")
    web_content = forms.CharField(widget=TinyMCE(attrs={'cols': 30, 'rows': 10}), required=True, label="Text na podstronie")
    has_pictures = forms.BooleanField(required=False, label="Czy posiada zdjęcia")
    pictures = forms.ModelMultipleChoiceField(queryset=Pictures.objects.filter(has_gallery=False).order_by('-timestamp'), required = False, label='Wybierz Zdjęcia ( z L-Shift / L-Ctrl wybierasz kilka )')
    has_files = forms.BooleanField(required=False, label="Czy posiada Załączniki")
    web_filles = forms.ModelMultipleChoiceField(queryset=Files.objects.order_by('-timestamp'), required = False, label='Wybierz Załączniki ( z L-Shift / L-Ctrl wybierasz kilka )')
    
    class Meta:
        model = Webs
        fields = ('web_name', 'web_content', 'has_pictures', 'pictures', 'has_files', 'web_filles')
        
class WebCatCreateForm(forms.ModelForm):
    web_cat_name = forms.CharField(required=True, label="Nazwa Głównej strony")
    webs = forms.ModelMultipleChoiceField(queryset=Webs.objects.all(), required = True, label='Wybierz podstrony ( z L-Shift / L-Ctrl wybierasz kilka )')
    class Meta:
        model = WebCategory
        fields = ('web_cat_name','webs')