from django import forms
from .models import Files

class FileForm(forms.ModelForm):
    file = forms.FileField()
    
    class Meta:
        model = Files
        fields = ['file'] 
        widgets = {
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
