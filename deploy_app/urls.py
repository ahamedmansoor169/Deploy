from django.urls import path
from deploy_app import views
urlpatterns = [
    path('', views.index, name="index"),
]