from django.urls import path
from . import views

urlpatterns = [
    path('ebook_list/', views.ebook_list, name='ebook_list'),
]
