## Create a Book Instance

```python

from bookshelf.models import Book

book = Book.objects.create(title="Nineteen Eighty-Four", author="George Orwell", publication_year=1949)
print(book.id)  # Output the book ID

# Expected output



```
