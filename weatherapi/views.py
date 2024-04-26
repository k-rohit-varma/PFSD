from django.shortcuts import render
import string
import random
import requests
from django.core.mail import send_mail
from django.contrib.sites.requests import RequestSite

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.template import loader

# Create your views here.
from .models import User ,UserFeedBack,SaveUser

def home(request):
    return render(request,'home.html')

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '9e32d96dd2ffa561218f3c7d8773ac3f'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1 = round(temperature - 273.15, 2)
            return render(request, 'weather.html',
                  {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
                error_message = 'City not found. Please try again.'
                return render(request, 'weather.html', {'error_message': error_message})
        

def Userweatherlogic(request):
    if request.method == 'POST':
        place = request.POST.get('place', '')
        e_mail=request.POST.get('e_mail')
        API_KEY = '9e32d96dd2ffa561218f3c7d8773ac3f'

        if not place:
            error_message = 'Please provide a city.'
            return render(request, 'weather.html', {'error_message': error_message})

        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            main_weather = data.get('weather', [])[0]
            temperature = data.get('main', {}).get('temp', 0)
            humidity = data.get('main', {}).get('humidity', 0)
            temperature_celsius = round(temperature - 273.15, 2)
            wind_speed = data.get('wind', {}).get('speed', 0)
            weather_description = main_weather.get('description', '')
            weather_icon = main_weather.get('icon', '')

            user=SaveUser(
                city=place,
                temperatue =   temperature_celsius,
                humidity=humidity,
                wind=wind_speed,
                weather=weather_description
            )
            user.save()
            subject = 'SampleMailFromDjangoApp'
            message = f"The current temperature in {place.upper()} is {temperature_celsius}°C."
            from_email = 'raise3327@gmail.com'
            recipient_list = [e_mail]
            send_mail(subject, message, from_email, recipient_list)
            # html_content ='<h1>This is content </h1>'

            # return render(request, 'email.html')

            return render(request, 'loginWeather.html', {
                'city': str.upper(place),
                'temperature1': temperature_celsius,
                'humidity': humidity,
                'wind_speed': wind_speed,
                'weather_description': weather_description,
                'weather_icon': weather_icon
            })
        else:
            error_message = f'Error fetching weather data. Status code: {response.status_code}'
            return render(request, 'loginWeather.html', {'error_message': error_message})
        
def weatherUser(request):
    return render(request,'loginWeather.html')        

def weatherinput(request):
    return render(request,'weather.html')

def register_user(request):
    if request.method == 'POST':
      #  print(request.POST)
        fullname = request.POST.get('fname')
        email = request.POST.get('umail')
        username = request.POST.get('uname')
        password = request.POST.get('upass')
        mobileno = request.POST.get('mnum')
        location = request.POST.get('address')
        user = User(
            fullname=fullname,
            email=email,
            username=username,
            password=password,
            mobileno=mobileno,
            location=location
        )
        user.save()
        return render(request, 'login.html')
    else:
        return render(request, 'userRegistration.html')

def login(request):
    return render(request ,'login.html')

def login_logic(request):
    user = User.objects.all()
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        flag = User.objects.filter(username=uname,password=pwd).values()
        if flag:
            return render(request,'loginWeather.html',{'name':uname})
        else:

            return render(request,'login.html')

def about(request):
    return render(request,'aboutus.html')
def successFeedback(request):
    return render(request,'successFeedback.html')

def feedback(request):
    return render(request,'feedback.html')
def feedback_logic(request):

    if request.method=="POST":
        suggestion = request.POST.get('suggestion')
        nostar =request.POST.get('rating')
        name=request.POST.get('uname')
        user=UserFeedBack(
            suggestion =suggestion,
            stars=nostar,
            name=name,
        )
        user.save()
        return render(request,'successFeedback.html')
    else:
        return render(request,'feedback.html')


def map(request):
    return render(request,'map.html')

def fiveday(request):
    return render(request,'fiveday.html')
