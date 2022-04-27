from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('article/<int:article_id>/', getArticle),
]
