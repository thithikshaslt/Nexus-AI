from django.urls import path
from .views import get_models, chat_completions, chat_view

urlpatterns = [
    path("chat/", chat_view, name="chat"),
    path("models/", get_models, name="get_models"),
    path("v1/chat/completions/", chat_completions, name="chat_completions"),
]
