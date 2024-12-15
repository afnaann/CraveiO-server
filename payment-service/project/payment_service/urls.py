
from .views import StripeCheckoutView
from django.urls import path


urlpatterns = [
    path('post/',StripeCheckoutView.as_view()),
]
