from django.urls import path
from .views import lista_posts

urlpatterns = [
    path('', lista_posts, name='lista-posts'),
]