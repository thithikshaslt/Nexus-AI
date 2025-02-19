from django.urls import path
from .views import get_models, chat_completions

urlpatterns = [
    path('models/', get_models, name='get_models'),
    path("v1/chat/completions", chat_completions, name="chat_completions"),
]
