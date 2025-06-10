from django.urls import path
from blog import views

urlpatterns = [  # Corrigido aqui
    path('', views.PostView.as_view(), name='home')  # Corrigido aqui
]