from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("index_to_noun_result",views.index_to_noun_result,name="index_to_noun_result"),
]