from re import template
from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Books, Orders
from users.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.core.mail import EmailMessage
from django.db.models import Sum


class BookListView(ListView):
    model = Books
    template_name = "shopping/home.html"
    context_object_name = "books"


class BookDetailView(DetailView):
    model = Books
    template_name = "shopping/book_details.html"
    context_object_name = "book"


def about(request):
    return render(request, "shopping/about.html", {"title": "about"})


class OrderListView(LoginRequiredMixin, ListView):
    model = Orders
    template_name = "shopping/orders.html"
    context_object_name = "orders"
    ordering = ["-purchasedate"]

    def get_queryset(self):
        return super().get_queryset().filter(userid=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        total_price = Orders.objects.filter(userid = self.request.user.id).aggregate(total=Sum('productid__price'))
        context["total_spending"] = total_price['total']       #passing total spent amount
        return context


@login_required
def OrderCreateView(request, bookid):
    if request.method == "POST":
        user = User.objects.filter(username=request.user).first()
        book = Books.objects.filter(id=bookid).first()

        if user.profile.money >= book.price:
            try:
                subject_mail = f"Purchased-{book.title}-ijshopping"
                body_mail = f"Hii! {request.user} Thank You for purchasing. Your e-book is attached with this email"
                from_mail = "ijshopping.books@gmail.com"
                to_mail = request.user.email
                msg = EmailMessage(subject_mail, body_mail, from_mail, [to_mail])   #EmailMessage('Subject of the Email', 'Body of the email', 'from@email.com', ['to@email.com'])
                msg.content_subtype = "html"
                book_path = book.file.path
                msg.attach_file(book_path)
                msg.send()
            except Exception:
                messages.warning(request, "An error has been occured,Please check whether your registered email is valid")
                return redirect('shop-home')

            user.profile.money -= book.price
            user.profile.save()
            order = Orders.objects.create(userid=user, productid=book)
            order.save()
            messages.success(request, "Order Successfull")
            return redirect("order-success")
        else:
            messages.warning(request, "Insufficient Balance in wallet")
            return redirect("shop-home")
    else:
        return render(request, "shopping/order_confirm.html")

@login_required
def order_success(request):
    return render(request, "shopping/order_success.html")
