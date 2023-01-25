from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='list'),
    path('update_task/<str:pk>/', update_task, name='update'),
    path('delete/<str:pk>/', delete_task, name='delete')
]