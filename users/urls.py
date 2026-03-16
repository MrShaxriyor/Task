from django.urls import path
from .views import signup, EmailLoginView

urlpatterns = [
    path('register/', signup),
    path('login/', EmailLoginView.as_view()),
]