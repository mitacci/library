from django.shortcuts import render, redirect

from djangoProject.library.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, AddBook, EditBook
from djangoProject.library.models import Book
from djangoProject.library.users import get_user


def show_home(request):
    profile = get_user()
    books = Book.objects.all()
    if not profile:
        return redirect('create profile')
    context = {
        'user': profile,
        'books': books,
    }
    return render(request, 'home-with-profile.html', context)


def add_book(request):
    if request.method == 'POST':
        form = AddBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddBook()
    context = {
        'form': form,
    }
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditBook(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditBook(instance=book)
    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'edit-book.html', context)


def book_details(request, pk):
    context = {
        'book': Book.objects.get(pk=pk)
    }
    return render(request, 'book-details.html', context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('index')


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'hidden': True,
    }
    return render(request, 'home-no-profile.html', context)


def show_profile(request):
    context = {
        'user': get_user(),
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    user = get_user()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditProfileForm(instance=user)

    context = {
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    user = get_user()
    books = Book.objects.all()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            books.delete()
            return redirect('index')
    else:
        form = DeleteProfileForm(instance=user)

    context = {
        'form': form,
    }
    return render(request, 'delete-profile.html', context)
