from django.urls import path
from . import views

urlpatterns = [
    path('', views.vision_test, name='vision_test'),
    path('results/', views.results, name='results'),
]
