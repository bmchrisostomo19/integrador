<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('curso/<int:id>', views.curso, name = 'curso'),
    path('aula/<int:id>', views.aula, name = 'aula'),
    path('comentarios/', views.comentarios, name= 'comentarios'),
    path('processa_avaliacao/', views.processa_avaliacao, name= 'processa_avaliacao')
=======
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('curso/<int:id>', views.curso, name = 'curso'),
    path('aula/<int:id>', views.aula, name = 'aula'),
    path('comentarios/', views.comentarios, name= 'comentarios'),
    path('processa_avaliacao/', views.processa_avaliacao, name= 'processa_avaliacao')
>>>>>>> 1651482b46c304b36ab1d5056382003c08636891
]