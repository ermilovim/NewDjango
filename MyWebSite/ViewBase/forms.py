from django import forms


class NameForm(forms.Form):
    add_new_id = forms.CharField(label='Your name', max_length=100)
