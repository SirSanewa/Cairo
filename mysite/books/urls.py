from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('book/<str:book_title>', views.book, name="book")
]
