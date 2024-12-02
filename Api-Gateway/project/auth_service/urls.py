from django.urls import path

from .views import LoginView, SignupView,GoogleAuthView


urlpatterns = [
    path('signup/',SignupView.as_view()),
    path('signin/',LoginView.as_view()),
    path('google/',GoogleAuthView.as_view()),
]
