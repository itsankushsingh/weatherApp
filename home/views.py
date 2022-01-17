from django.shortcuts import render
import requests

# Create your views here.


def home(request):

    city = request.GET.get('city','Lucknow')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a66a72789fa3c4c160c771a71ce5cba2'
    data = requests.get(url).json()
    pyload = {
              
              'city': data['name'],
              'weather': data['weather'][0]['main'],
              'icon': data['weather'][0]['icon'],
              'k_temp': data['main']['temp'],
              'c_temp': round(data['main']['temp'] -273,2),
              'pressure': data['main']['pressure'],
              'humidity': data['main']['humidity'],
              'description' : data['weather'][0]['description'],
              
        }
    context = {'data': pyload}
    return render(request, 'index.html', context)
