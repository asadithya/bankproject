from.import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='demo'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='user-login'),
    path('newpage/', views.newpage, name='newpage'),
    path('form/', views.form, name='bank-form'),
    path('msg/',views.msg,name='msg'),
    path('get_branches' , views.get_branches , name="get-branch") ,
    path('logout'  , views.logout , name="logout")
]