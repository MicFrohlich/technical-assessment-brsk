from django.urls import path
from .views import replace_words_api

urlpatterns = [
    path('replace-words/', replace_words_api, name='replace-words-api'),
]