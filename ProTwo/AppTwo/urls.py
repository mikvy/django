from django.contrib import admin
from django.urls import path
from AppTwo import views
urlpatterns = [

    path('help/',views.help),
    path('',views.index)
]
