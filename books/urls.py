from django.urls import path, include
from .views import BookListView, BookDetailView, SearchResultsListView


urlpatterns = [
  path('', BookListView.as_view(), name="book_list"),
  path('<int:pk>/detail', BookDetailView.as_view() , name = 'book_detail'),
  path('search/', SearchResultsListView.as_view(), name='search_results'),

]