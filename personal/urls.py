from django.urls import path
from . import views

urlpatterns = [
    path('personal_app/', views.personal, name='members')
]
