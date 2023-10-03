import datetime

from django import forms

from myapp2.models import Author


class Author_form(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField()
    biography = forms.CharField(max_length=300)
    birthday = forms.DateField(initial=datetime.date.today)


class Article_form(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(max_length=300)

    author = Author.objects.filter()
    context = []
    for item in author:
        context.append((item.id, item.full_name()))

    author = forms.ChoiceField(choices=context)
    category = forms.CharField(max_length=100)
    publish = forms.BooleanField()
