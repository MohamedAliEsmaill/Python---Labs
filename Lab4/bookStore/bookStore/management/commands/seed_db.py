
from django.core.management.base import BaseCommand
from ... import seed_data
from  ...models import Book

class Command(BaseCommand):
    help = 'Seed the database with 100 books'

    def handle(self, *args, **kwargs):
        books_data = seed_data.generate_books(100)
        for book_data in books_data:
            book = Book.objects.create(**book_data)
            self.stdout.write(self.style.SUCCESS(f'Successfully created book "{book.title}"'))
