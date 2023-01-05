from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstpageView, name='firstpage_url'),
    path('base/<str:company>/',views.baseView,name='base_url'),
    path('login/', views.loginView, name='login_url'),
    path('signup/' , views.signupView,name='signup_url'),
    path('mv/',views.msgView,name='msg_url'),
    path('at/', views.addtaskView, name='addtask_url'),
]