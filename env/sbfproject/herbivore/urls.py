from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = "home"),
    path('animal/', views.AnimalView.as_view(), name = "animal"),
    path('<int:id>', views.AddAndDeleteAnimalModel.as_view()),
]