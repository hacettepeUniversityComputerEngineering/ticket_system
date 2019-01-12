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


class SelectPersonCount(forms.Form):
    CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10))
    person_count = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'input-group',
    }), choices=CHOICES)


class PaymentForm(forms.Form):
    name_surname = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Name Surname',
        }
    ))
    tckn = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'TCKN',
        }
    ))
    e_mail = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'E-mail',
        }
    ))
    credit_card_numbers = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Credit Card Number',
        }
    ))
    phone_number = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Phone Number',
        }
    ))
    last_usage_date = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Last Usage Date',
        }
    ))
    security_number = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Security Number',
        }
    ))
