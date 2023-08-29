from django.urls import path
from . import views

urlpatterns = [
    path('', views.getdata),
    path('create', views.addprocessmaster),
    path('read/<str:pk>', views.getdata),
    path('update/<str:pk>', views.updateprocessmaster),
    path('delete/<str:pk>', views.deleteprocessmaster),
]
