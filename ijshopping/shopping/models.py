from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Books(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(default="default.jpg", upload_to="book_pics")
    file = models.FileField(default="default_book.pdf", upload_to="book_files")

    def get_absolute_url(self):
        return reverse("book-detail", kwargs={"pk": self.pk})


class Orders(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    productid = models.ForeignKey(Books, on_delete=models.CASCADE)
    purchasedate = models.DateTimeField(default=timezone.now)

