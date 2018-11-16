from django import forms
from .models import *


class NewIdForm(forms.ModelForm):
    addnewid = forms.CharField(label='Введите идентификатор', max_length=100)

    # class Meta:
    #     model = NewIdForm
    #     exclude = [""]

