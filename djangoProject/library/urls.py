from django.urls import path
from djangoProject.library.views import show_home, \
    add_book, edit_book, book_details, delete_book, \
    create_profile, show_profile, edit_profile, delete_profile

urlpatterns = [
    path('', show_home, name='index'),

    path('add/', add_book, name='add book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('details/<int:pk>/', book_details, name='book details'),
    path('delete/<int:pk>/', delete_book, name='delete_book'),

    path('profile/create/', create_profile, name='create profile'),
    path('profile/', show_profile, name='show profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
]