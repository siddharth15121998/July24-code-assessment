from . import views
from django.urls import path,include

urlpatterns = [
    path('add/',views.addStudent,name='addStudent'),
]