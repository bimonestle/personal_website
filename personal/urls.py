from django.urls import path
from . import views

urlpatterns = [
    path('personal_app/', views.personal, name='members'),
    path('calculate_average_sessions/', views.calculate_avg_sessions, name='calc_avg_sess')
]
