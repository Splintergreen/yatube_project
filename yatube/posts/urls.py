from django.urls import path

from . import views


urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страницы сообществ
    path('groups/', views.groups_list),
    # Страница конкретного сообщества
    path('groups/<slug:any_slug>/', views.groups_detail),
]
