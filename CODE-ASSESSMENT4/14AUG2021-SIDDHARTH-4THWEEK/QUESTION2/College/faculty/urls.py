from . import views
from django.urls import path,include
urlpatterns = [
    path('add/',views.addFaculty,name='addFaculty'),
]