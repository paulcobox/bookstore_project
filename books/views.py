from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin # new
from django.db.models import Q # new
# Create your views here.


class BookListView(LoginRequiredMixin, ListView):
  model = Book
  template_name = "books/book_list.html"
  context_object_name = 'book_list'
  login_url = 'login' # new


class BookDetailView(LoginRequiredMixin, DetailView):
  model = Book
  template_name = "books/book_detail.html"
  context_object_name = 'book'
  login_url = 'login' # new


class SearchResultsListView(ListView):
  model = Book
  template_name = "books/search_results.html"
  context_object_name = "book_list"
  # queryset = Book.objects.filter(title__icontains='django')

  def get_queryset(self): # new
    query = self.request.GET.get('q')
    return Book.objects.filter(
      Q(title__icontains=query) | Q(author__icontains=query)
    )