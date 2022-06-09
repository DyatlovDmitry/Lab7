from django.urls import re_path, path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordChangeView
from polls import views

urlpatterns = [
    path('Login/', LoginView.as_view(), name='login'),
    #re_path(r'^PageForPosts$', , name='login'),
    # path('login/', views.login, name='login'),
    path('Localization/', views.Localization,name='Localization'),
    path('PageForPosts/', views.PageForPosts, name='PageForPosts'),
    # re_path(r'^likePost/$', views.likePost, name='likePost'),
    # path('like_post/', views.like_post, name='like_post'),
    # re_path(r'^FirstPage/$', views.FirstPage, name='FirstPage'),
    path('FirstPage/', views.FirstPage, name='FirstPage'),
    # re_path(r'^SecondPage/$', views.SecondPage, name='SecondPage'),
    path('SecondPage/', views.SecondPage, name='SecondPage'),
    path('ThirdPage/', views.ThirdPage, name='ThirdPage'),
    path('Validation/', views.Validation, name='Validation'),
    path('End/', views.End, name='End'),
    path('Bot/', views.Bot, name='Bot')
]
