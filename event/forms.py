from django import forms
from event.models import Category, City


class SearchForm(forms.Form):
    name = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Search event',
        }
    ))


class SelectCategory(forms.Form):
    CHOICES = ()
    categories = tuple(Category.objects.all().values_list())
    for i in categories:
        CHOICES = ((i[1], i[1]),) + CHOICES
    category_name = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'input-group',
    }), choices=CHOICES)


class SelectCity(forms.Form):
    CHOICES = ()
    cities = tuple(City.objects.all().values_list())
    for i in cities:
        CHOICES = ((i[1], i[1]),) + CHOICES
    city_name = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'input-group',
    }), choices=CHOICES)
