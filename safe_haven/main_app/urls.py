from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('journals/new/', views.CreateJournal.as_view(), name='CreateJournal'),
    path('journals/all/', views.IndexJournal.as_view(), name='IndexJournal'),
    path('journals/<int:pk>/', views.DetailJournal.as_view(), name='Journal_detail'),
    path('journals/<int:pk>/update/', views.UpdateJournal.as_view(), name='Journal_update'),
    path('journals/<int:pk>/delete/', views.DeleteJournal.as_view(), name='Journal_delete'),
]
