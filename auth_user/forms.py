from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=30, required=True)
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Nie znaleziono użytkownika")
        return username
    
    def clean_password(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        if user is not None and not user.check_password(password):
            raise forms.ValidationError("Podałeś/aś złe hasło")
        elif user is None:
            pass
        else:
            return password

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Hasło', \
        max_length=30, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Powtórz Hasło', \
        max_length=30, required=True)
    username = forms.CharField(max_length=50, required=True, label="Nazwa Użytkownika")
    
    class Meta:
        model = User
        fields = ['username']
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
    
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Hasła różnią się')
        return password2
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user