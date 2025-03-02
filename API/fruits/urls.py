from django.urls import path
from . import views

urlpatterns = [
    path("fruit/", views.fruit_list.as_view(), name=""),
    path("fruit_crud/<int:pk>/", views.fruit_crud.as_view(), name="crud"),
]
