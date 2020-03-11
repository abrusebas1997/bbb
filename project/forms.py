from django import forms
from project.models import Book


class BookForm(forms.ModelForm):
     class Meta:
    # """ Render and process a form based on the Book model. """
        model = Book
        fields = ("title", "content", "author")
