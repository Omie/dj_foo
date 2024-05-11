from django.db import models


class Book(models.Model):
    # represents a book from books.toscrape.com
    title = models.CharField(max_length=250)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.title

