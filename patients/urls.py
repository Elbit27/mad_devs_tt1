from django.urls import path
from . import views


urlpatterns = [
    path('', views.PatientListAPIView.as_view()),
]