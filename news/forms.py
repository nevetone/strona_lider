from tinymce import TinyMCE
from django import forms
from .models import News, MainNews

class TinyMCEWidget(TinyMCE):
    def use_required_atribute(self, *args):
        return False

class NewsForm(forms.ModelForm):

    content = forms.CharField(widget=TinyMCE(attrs={'cols': 30, 'rows': 10}), required=False, label="Podstrona")
    
    class Meta:
        model = News
        fields = ('title', 'overview','thumbnail', 'category','web_name', 'has_own_web','content','has_gallery','gallery',)


class MainNewsForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 30, 'rows': 10}), required=False, label="Podstrona")
    
    class Meta:
        model = MainNews
        fields = ('title', 'overview','thumbnail', 'category','web_name', 'has_own_web','has_gallery','gallery',)