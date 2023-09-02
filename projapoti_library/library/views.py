from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404, render, redirect
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from .models import Book

from rest_framework import viewsets
from .models import Book
from .models import Wishlist
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def custom_404(request, exception):
    return render(request, '404.html', {}, status=404)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'registration/login.html')


def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        user_wishlist = Wishlist.objects.filter(
            user=user).select_related('book')

        context['user_wishlist'] = user_wishlist
        return context


@login_required
def add_to_wishlist(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    user = request.user

    if not Wishlist.objects.filter(user=user, book=book).exists():
        Wishlist.objects.create(user=user, book=book)

    return redirect('dashboard')

@login_required
def remove_from_wishlist(request, book_id):
    user = request.user
    Wishlist.objects.filter(user=user, book__id=book_id).delete()
    return redirect('dashboard')