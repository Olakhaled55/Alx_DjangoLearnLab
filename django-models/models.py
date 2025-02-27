from django.db import models

# Create your models here.
from django.db import models

# نموذج المؤلف
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# نموذج الكتاب
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# نموذج المكتبة
class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

# نموذج أمين المكتبة
class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
