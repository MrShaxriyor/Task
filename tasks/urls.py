from django.urls import path
from .views import TaskListCreateAPIView, TaskDetailAPIView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("tasks/", TaskListCreateAPIView.as_view()),
    path("tasks/<int:pk>/", TaskDetailAPIView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]