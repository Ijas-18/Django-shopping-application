from django.contrib import admin

from .models import Books,Orders

admin.site.register(Books)
admin.site.register(Orders)