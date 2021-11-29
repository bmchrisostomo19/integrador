<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('valida_cadastro/', views.valida_cadastro, name="valida_cadastro"),
    path('valida_login/', views.valida_login, name="valida_login"),
    path('sair/', views.sair, name = 'sair')
=======
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('valida_cadastro/', views.valida_cadastro, name="valida_cadastro"),
    path('valida_login/', views.valida_login, name="valida_login"),
    path('sair/', views.sair, name = 'sair')
>>>>>>> 1651482b46c304b36ab1d5056382003c08636891
]