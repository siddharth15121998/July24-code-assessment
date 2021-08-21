from . import views
from django.urls import path,include

urlpatterns = [
   
    path('register/',views.registerlibrarian,name='registerlibrarian'),
    path('login/',views.loginlibrarian,name='loginlibrarian'),

    path('add/',views.add_apii,name='add_apii'),
    path('viewall/',views.viewall_apii,name='viewall_apii'),
    path('view/<ecode>',views.view_apii,name='view_apii'),
]