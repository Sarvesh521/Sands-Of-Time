from django.urls import path
from . import views 

urlpatterns = [
    path('login/', views.loginPage, name="login"), 
    path('logout/', views.logoutUser, name="logout"), 
    path('register/', views.registerPage, name="register"),
    path('participant',views.participant_home,name="participant_home"),
    # path('code',views.code,name="code")
]