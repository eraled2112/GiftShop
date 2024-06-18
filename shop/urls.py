from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    path('contact/', contact),
    path('shop/<int:id>', shop),
]
