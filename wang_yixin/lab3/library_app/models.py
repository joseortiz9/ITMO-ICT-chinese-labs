from django.db import models

# Create your models here.


class Book(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    book_name = models.CharField(max_length=240)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, blank=True)
    book_types = (
        ('n', 'novel'),
        ('m', 'magazine'),
        ('n', 'newspaper'),
        ('t', 'tools'),
    )
    Type = models.CharField(max_length=1, choices=book_types)
    year_of_pub = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['book_name']

    def __str__(self):
        return self.book_name


class Reader(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    sex_types = (
        ('m', 'man'),
        ('w', 'woman'),
    )
    sex = models.CharField(max_length=1, choices=sex_types)
    birthday = models.DateField(null=False)
    passport = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.first_name


class BookInstance(models.Model):
    id = models.IntegerField(primary_key=True)
    id_book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default=False)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.first_name
