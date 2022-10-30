from django.forms import ModelForm, TextInput
from app.models import Profile


class ProfileForms(ModelForm):
    class Meta:
        model = Profile
        fields = ['PixivId', 'Email', 'Nick']
        widgets = {
            'PixivId': TextInput(attrs={'class': 'form-control', 'placeholder': 'PixivId'}),
            'Email': TextInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Email'}),
            'Nick': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nick'})
        }