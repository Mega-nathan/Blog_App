from django import forms
from .models import blog 

class BlogForm(forms.ModelForm):
    class Meta:
        model = blog  
        fields = '__all__'
        widgets={
            'userName':forms.TextInput(attrs={'class':'form-inputs'}),
            'title':forms.TextInput(attrs={'class':'form-inputs'}),
            'category':forms.Select(attrs={'class':'form-choices'}),

        }