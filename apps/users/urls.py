from django.urls import path

from apps.users.views import RegisterAPIView

urlpatterns = [
    path('user/register/', RegisterAPIView.as_view(), name='register')
]
