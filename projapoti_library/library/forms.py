from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Borrowing, Review


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


class BorrowingForm(forms.ModelForm):
    class Meta:
        model = Borrowing
        fields = ['book', 'return_date']
        book_id = forms.IntegerField(widget=forms.HiddenInput())


class ReturningReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
