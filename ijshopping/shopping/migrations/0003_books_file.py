# Generated by Django 3.2.6 on 2021-11-04 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_books_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='file',
            field=models.FileField(default='default_book.pdf', upload_to='book_files'),
        ),
    ]
