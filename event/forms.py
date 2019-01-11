from django import forms


class SearchForm(forms.Form):
    name = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Search event',
        }
    ))
