from django.urls import path
from . import views

urlpatterns = [
    path('', views.personal, name='personal'),
    path('calculate_average_sessions/', views.calculate_avg_sessions, name='calc_avg_sess'),
    path("testing/", views.testing, name="testing")
]
