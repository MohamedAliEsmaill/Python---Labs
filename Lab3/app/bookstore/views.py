from django.shortcuts import render, redirect

# Create your views here.

books = [
    {
        'id': 1,
        'title': 'Django for Beginners',
        'author': 'William S. Vincent',
        'published_date': '2020-01-01',
        'description': 'Django for Beginners is a project-based introduction to Django, the popular Python-based web framework. Suitable for total beginners who have never built a website before as well as professional programmers looking for a fast-paced guide to modern web development and Django fundamentals.'
    },
    {
        'id': 2,
        'title': 'Django for APIs',
        'author': 'William S. Vincent',
        'published_date': '2020-01-01',
        'description': 'Django for APIs is a project-based guide to building modern APIs with Django & Django REST Framework. It is suitable for intermediate web developers who are new to Django or experienced Django developers who want to create RESTful APIs.'
    }
]

def index(request):
    return render(request, 'bookstore/index.html', context={'books': books})

def show(request,id):
    for book in books:
        if book['id'] == id:
            return render(request, 'bookstore/show.html', context={'book': book})

def create(request):
    return render(request, 'bookstore/create.html')

def edit(request, id):
    for book in books:
        if book['id'] == id:
            return render(request, 'bookstore/edit.html', context={'book': book})

def delete(request, id):
    for book in books:
        if book['id'] == id:
            books.remove(book)
            return redirect('index')


def store(request):
    books.append({
        'id': len(books) + 1,
        'title': request.POST['title'],
        'author': request.POST['author'],
        'published_date': request.POST['published_date'],
        'description': request.POST['description']
    })
    return redirect('index')

def update(request, id):
    for book in books:
        if book['id'] == id:
            book['title'] = request.POST['title']
            book['author'] = request.POST['author']
            book['published_date'] = request.POST['published_date']
            book['description'] = request.POST['description']
            return redirect('index')