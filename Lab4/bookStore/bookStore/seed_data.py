import random

def generate_books(num_books):
    books_data = []
    for i in range(num_books):
        title = f'Book {i+1}'
        author_name = f'Author {random.randint(1, 10)}'
        description = f'Description for Book {i+1}'
        book_type = f'Type {random.randint(1, 5)}'
        rate = random.randint(1, 5)
        views = random.randint(50, 500)
        book_data = {
            'title': title,
            'author_name': author_name,
            'description': description,
            'type': book_type,
            'rate': rate,
            'views': views
        }
        books_data.append(book_data)
    return books_data
