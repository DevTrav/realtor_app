from django.urls import path
from .views import SignupView


urlspatterns = [
    path('Signup', SignupView.as_view()),
]