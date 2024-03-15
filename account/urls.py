from django.urls import path
from .views import SignUpView, LoginView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair')
]