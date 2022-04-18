from django.urls import path
from .views import home_view, name_view

urlpatterns = [
    path('', home_view, name='home'),
    path('name/<name>/', name_view),
]