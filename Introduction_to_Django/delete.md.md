```python

from bookshelf.models import Book

retrieved_book.delete()
all_books = Book.objects.all()
print(list(all_books)) # Should return an empty list
```
