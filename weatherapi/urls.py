
from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('',views.home,name='home_page'),
    path('weatherlogic',views.weatherlogic,name="weatherlogic"),
    path('weatherinput',views.weatherinput,name='weatherinput'),
    path('register_user', views.register_user, name="register_user"),
    path('login_page', views.login, name="login_page"),
    path('login_logic', views.login_logic, name='login_logic'),
    path('about_page',views.about,name="about_page"),
    path('weatherLoginlogic',views.Userweatherlogic,name="weatherLoginlogic"),
    path('weatherUser',views.weatherUser,name="weatherUser"),
    path('feedback',views.feedback,name="feedback"),
    path('feedback_logic',views.feedback_logic,name="feedback_logic"),
    path('successFeedback',views.successFeedback,name="successFeedback"),
    path('map_page',views.map,name="map_page"),
    path('five-day',views.fiveday,name="five-day"),
]
