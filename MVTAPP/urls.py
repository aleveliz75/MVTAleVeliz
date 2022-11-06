from django.urls import path
from MVTAPP.views import get_familiares

urlpatterns = [
    path('', get_familiares)
]