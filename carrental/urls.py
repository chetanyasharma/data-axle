from django.urls import path

from . import views

urlpatterns = [
    path('rental_registar', views.RentRegistrationView.as_view()),
    path('return_car', views.RentRegistrationView.as_view()),
]
