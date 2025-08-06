from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("register/", views.register, name="register"),
    path('prisijungti/', LoginView.as_view(template_name='prisijungti.html'), name='prisijungti'),
    path('atsijungti/', LogoutView.as_view(next_page='prisijungti'), name='atsijungti'),
    path('slaptas/', views.slaptas, name='slaptas'),
]
