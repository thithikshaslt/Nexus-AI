from django.urls import path
from .views import get_models, chat_completions, chat_view, chat_upload, file_upload

urlpatterns = [
    path("chat/", chat_view, name="chat"),
    path("models/", get_models, name="get_models"),
    path("v1/chat/completions/", chat_completions, name="chat_completions"),
    path("api/v1/chat/upload/", chat_upload, name="chat_upload"),
]
