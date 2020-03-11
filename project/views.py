from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse, reverse_lazy
from project.forms import BookForm
from project.models import Book
from django.http import HttpResponse, HttpResponseRedirect



class Home(generic.CreateView):
    def get(self, request):
        return render(request, 'base.html')

class BookListView(generic.ListView):
    """ Renders a list of all projects. """
    model = Book

    def get(self, request):
        """ GET a list of projects. """
        books = self.get_queryset().all()
        return render(request, 'list.html', {
          'books': books
        })

class BookDetailView(generic.DetailView):
    """ Renders a specific project based on it's slug."""
    model = Book

    def get(self, request, slug):
        """ Returns a specific projects project by slug. """
        book = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'book.html', {
          'book': book
        })
class BookCreateView(generic.CreateView):
    form_class = BookForm
    template_name = "new_book.html"

    def post(self, request, *args, **kwargs):
        form = BookForm(request.POST)
        if form.is_valid():
            project = form.save()
            project.save()
            return HttpResponseRedirect(reverse_lazy("book-details-project", args=[project.slug]))

class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title','content']
    template_name = 'new_book.html'

class BookDeleteView(generic.DeleteView):
    model = Book
    success_url = reverse_lazy('book-list-project')
    template_name = 'confirm_delete.html'
