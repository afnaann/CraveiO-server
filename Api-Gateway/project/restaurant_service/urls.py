from django.urls import path

from .views import MenuView, RestaurantView,CategoryView


urlpatterns = [
    path('join/',RestaurantView.as_view()),
    path('category/',CategoryView.as_view()),
    path('menu/',MenuView.as_view()),
    path('menu/<int:pk>/',MenuView.as_view()),
]
