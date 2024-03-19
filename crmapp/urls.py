from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login', views.login, name='login'),
    path('sign', views.sign, name='sign'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('archive', views.archive, name='archive'),
    path('page1', views.page1, name='page1'),
    path('page2', views.page2, name='page2'),

]
