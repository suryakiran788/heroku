
from django.urls import path
from . import views
urlpatterns = [
    path('', views.myhome,name="myhome"),
    path('page1', views.page1,name="page1"),
    path('button', views.button_bootstrap,name="button"),
    path('grid', views.grid_bootstrap,name="grid")
]
