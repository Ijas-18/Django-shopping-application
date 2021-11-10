from django.urls import path
from . import views
from .views import BookListView, BookDetailView, OrderListView

urlpatterns = [
    path("", BookListView.as_view(), name="shop-home"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("book/order/<int:bookid>/", views.OrderCreateView, name="book-order"),
    path("order/success/", views.order_success, name="order-success"),
    path("orders/", OrderListView.as_view(), name="order-list"),
    path("about/", views.about, name="shop-about"),
]
