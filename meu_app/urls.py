from django.urls import path
from meu_app.views import index

urlpatterns = [
    path('', index)
]