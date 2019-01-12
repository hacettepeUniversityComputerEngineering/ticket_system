from django import forms


class SearchForm(forms.Form):
    name = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Search event',
        }
    ))


class SelectCategory(forms.Form):
    CHOICES = (('1', 'First',), ('2', 'Second',))
    name = forms.ChoiceField(widget=forms.Select(attrs={
            'class': 'input-group',
        }), choices=CHOICES)


class SelectCity(forms.Form):
    CHOICES = (('1', 'First',), ('2', 'Second',))
    name = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'input-group',
    }), choices=CHOICES)
