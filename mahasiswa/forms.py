from django import forms
from .models import Data_mhs

class BiodataMhs(forms.ModelForm):
    class Meta:
        model = Data_mhs
        fields = '__all__'
