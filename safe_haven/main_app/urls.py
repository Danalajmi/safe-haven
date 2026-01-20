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

    path('articles/all', views.IndexArt.as_view(), name='IndexArt'),
    path('articles/new', views.CreateArt.as_view(), name='CreateArt'),
    path('articles/<int:pk>', views.DetailArt.as_view(), name='Art_detail'),
    path('articles/<int:pk>/update', views.UpdateArt.as_view(), name='Art_update'),
    path('articles/<int:pk>/delete', views.DeleteArt.as_view(), name='Art_delete'),

]
