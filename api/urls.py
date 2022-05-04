from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getLights),
    path('api/lights/<str:pk>/delete/', views.deleteLight),
    path('api/lights/', views.getLights),
    path('api/lights/<str:pk>', views.getLight),
    path('api/lights/create/', views.createLight),
    path('api/lights/<str:pk>/update/', views.updateLight),

    path('card/create', views.createCard),
    path('card/', views.getCardCodes),
    path('card/<str:pk>', views.getCardCode),
]
