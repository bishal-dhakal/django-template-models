from django.contrib import admin
from django.urls import path
from . import views

urlpatterns= [
    path('index/',views.index, name="index"),
    # path('index/',views.Index.as_view(?, name="index")
    path('contact/',views.contact, name="contact"),

    #auth endpoint
    path('signup/',views.RegisterView.as_view(),name='signup'),
    path('session/',views.testsessions,name='sessiontest'),
]