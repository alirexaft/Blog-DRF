from django.urls import path
from .views import UserCreation, LogoutAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('signup/', view=UserCreation.as_view()),
    path('login/', view=obtain_auth_token),
    path('logout/', view=LogoutAPIView.as_view())
]
