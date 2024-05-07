from django.urls import path
from user import views

urlpatterns = [
    path("",views.index, name="index"),
    path('<int:user_id>/', views.index2, name="index2" )
]