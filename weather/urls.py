from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('item/<int:pk>/delete', views.delete_city, name='delete_city'),
]
