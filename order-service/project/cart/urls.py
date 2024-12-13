from django.urls import path

from .views import CartView, QuantityView


urlpatterns = [
    path('post/',CartView.as_view()),
    path('quantity/',QuantityView.as_view()),
    path('get/<int:pk>/',CartView.as_view()),
]
