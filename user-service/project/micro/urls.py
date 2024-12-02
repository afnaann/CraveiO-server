from django.urls import path
from .views import GoogleLoginView, SignupView, UserStatusView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/',SignupView.as_view()),
    path('signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('google/', GoogleLoginView.as_view()),
    path('status/', UserStatusView.as_view()),
]
