from django.urls import re_path, include, path

from .views import RegistrationAPIView
from .views import LoginAPIView

urlpatterns = [
    path('user/register/', RegistrationAPIView.as_view()),
    path('user/login/', LoginAPIView.as_view()),
]