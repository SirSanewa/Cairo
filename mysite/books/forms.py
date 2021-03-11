from django import forms


class NameForm(forms.Form):
    book_title = forms.CharField(label="book_title", max_length=40)
    book_author = forms.CharField(label="book_author", max_length=40)
