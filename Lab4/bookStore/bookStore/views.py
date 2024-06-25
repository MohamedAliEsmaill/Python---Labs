from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Book
from .form import BookForm


def index(request):
    return render(request, 'main/base_layout.html')

def bookstore_list(request):
    books_list = Book.objects.all()
    paginator = Paginator(books_list, 10)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'bookstore_list.html', {'page_obj': page_obj})

def book_add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books-list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def book_details(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'book_details.html', {'book': book})

def book_update(request, slug):
    book = Book.objects.get(slug=slug)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books-list')
    else:
        form = BookForm(instance=book)
    return render(request, 'update_book.html', {'form': form, 'book': book})

def book_delete(request, slug):
    book = Book.objects.get(slug=slug)
    book.delete()
    return redirect('books-list')
