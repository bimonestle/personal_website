from django.urls import path
from . import views

urlpatterns = [
    path("", views.calc_avg_sess, name="calc_avg_sess")
]