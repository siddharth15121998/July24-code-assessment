from . import views
from django.urls import path,include

urlpatterns = [
   
    path('',views.registerbooks,name='registerbooks'),

    path('add/',views.add_api,name='add_api'),
    path('viewall/',views.viewall_api,name='viewall_api'),
    path('view/<name>',views.view_api,name='view_api'),
]