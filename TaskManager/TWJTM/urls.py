from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstpageView, name='firstpage_url'),
    path('kn/<str:company>/',views.karvenagarView,name='karvenagar_url'),
    path('tbc/<str:company>/', views.karvenagarView, name='tbc_url'),

    path('login/<str:company>/', views.loginView, name='login_url'),
    path('signup/' , views.signupView,name='signup_url'),
    path('signout/', views.signupView, name='signout_url'),
    path('mv/',views.msgView,name='msg_url'),
    path('ad/<str:company>/', views.addDataView, name='addData_url'),
    path('vd/', views.viewDataView, name='viewdata_url'),
]