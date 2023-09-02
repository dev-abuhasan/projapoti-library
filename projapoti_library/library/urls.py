from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('add_to_wishlist/<int:book_id>/',
         views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:book_id>/',
         views.remove_from_wishlist, name='remove_from_wishlist'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
