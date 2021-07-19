"""Определяет схемы URL для Learning_logs."""
from django.urls import path
from . import views

urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    #  вывод всех тем
    path('topics/', views.topics, name='topics'),
    #  Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Страница для добавления новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
    # Страницы для добавления новой записи
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Страницы для редактирования записи
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Страница для удаления темы
    path('topics/<int:topic_id>/delete_topic/', views.delete_topic, name='delete_topic'),
    # Страница для удаления записи
    path('edit_entry/<int:entry_id>/delete_entry/', views.delete_entry, name='delete_entry'),
]