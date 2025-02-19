from django.urls import path
from .views import get_models

urlpatterns = [
    path('models/', get_models, name='get_models'),
]
