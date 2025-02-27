import os
import django

# ضبط إعدادات المشروع قبل استخدام ORM
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

# استيراد النماذج بعد ضبط Django
from relationship_app.models import Author, Book, Library, Librarian

# مثال لاستعلام
books = Book.objects.all()
for book in books:
    print(book.title, book.author.name)

import django
import os

# ضبط إعدادات Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1️⃣ إنشاء بيانات تجريبية
author1 = Author.objects.create(name="Ahmed Khaled Tawfik")
author2 = Author.objects.create(name="Naguib Mahfouz")

book1 = Book.objects.create(title="Utopia", author=author1)
book2 = Book.objects.create(title="Metro", author=author1)
book3 = Book.objects.create(title="The Harafish", author=author2)

library1 = Library.objects.create(name="Cairo Library")
library1.books.add(book1, book2)  # إضافة كتب إلى المكتبة

library2 = Library.objects.create(name="Alexandria Library")
library2.books.add(book3)

librarian1 = Librarian.objects.create(name="Ali", library=library1)
librarian2 = Librarian.objects.create(name="Omar", library=library2)

# 2️⃣ استعلام: جلب جميع الكتب لمؤلف معين
author_books = Book.objects.filter(author=author1)
print(f"Books by {author1.name}: {[book.title for book in author_books]}")

# 3️⃣ استعلام: جلب جميع الكتب في مكتبة معينة
library_books = library1.books.all()
print(f"Books in {library1.name}: {[book.title for book in library_books]}")

# 4️⃣ استعلام: جلب أمين المكتبة لمكتبة معينة
librarian = Librarian.objects.get(library=library1)
print(f"Librarian of {library1.name}: {librarian.name}")
import os
import django

# ضبط إعدادات Django لاستخدام ORM في هذا الملف
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    """ استعلام عن جميع الكتب التي كتبها مؤلف معين """
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return f"المؤلف '{author_name}' غير موجود."

def list_books_in_library(library_name):
    """ استعلام عن جميع الكتب داخل مكتبة معينة """
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # العلاقة ManyToMany
        return books
    except Library.DoesNotExist:
        return f"المكتبة '{library_name}' غير موجودة."

def get_librarian_for_library(library_name):
    """ استعلام عن أمين المكتبة المسؤول عن مكتبة معينة """
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian  # العلاقة OneToOne
    except Library.DoesNotExist:
        return f"المكتبة '{library_name}' غير موجودة."
    except Librarian.DoesNotExist:
        return f"لا يوجد أمين مكتبة معين للمكتبة '{library_name}'."

if __name__ == "__main__":
    # تجربة الاستعلامات
    author_name = "J.K. Rowling"
    library_name = "Central Library"
    
    print(f"📚 كتب المؤلف {author_name}:")
    for book in get_books_by_author(author_name):
        print(f"- {book.title}")

    print(f"\n📖 الكتب في مكتبة {library_name}:")
    for book in list_books_in_library(library_name):
        print(f"- {book.title}")

    print(f"\n👨‍💼 أمين مكتبة {library_name}:")
    librarian = get_librarian_for_library(library_name)
    print(librarian if isinstance(librarian, str) else librarian.name)
