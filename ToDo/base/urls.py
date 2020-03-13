from django.urls import path
from base.views import Home, UpdatePage, DeletePage

app_name = 'base'
urlpatterns = [
    path('', Home, name='list'),
    path('update/<int:pk>/', UpdatePage, name='update'),
    path('delete/<int:pk>/', DeletePage, name='delete'),

]
