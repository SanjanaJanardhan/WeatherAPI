from django.shortcuts import render
import requests
from .forms import CityForm
from config import WEATHER_API_KEY, WEATHER_API_URL, FORECAST_WEATHER_API_URL, HISTORICAL_WEATHER_API_URL

def home(request):
    form = CityForm()

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']

            current_weather_url = f"{WEATHER_API_URL}?key={WEATHER_API_KEY}&q={city}"
            response = requests.get(current_weather_url)
            data = response.json()

            if response.status_code == 200:
                return render(request, 'weather.html', {'city': city, 'weather': data})
            else:
                error_message = data.get('error', {}).get('message', 'Unknown error')
                return render(request, 'home.html', {'form': form, 'error_message': error_message})

    return render(request, 'home.html', {'form': form})

def forecast_weather(request, city):
    forecast_weather_url = f"{FORECAST_WEATHER_API_URL}?key={WEATHER_API_KEY}&q={city}&days=3"
    response = requests.get(forecast_weather_url)
    data = response.json()

    if response.status_code == 200:
        forecast_data = data['forecast']['forecastday']
        return render(request, 'forecast_weather.html', {'city': city, 'forecast_data': forecast_data})
    else:
        error_message = data.get('error', {}).get('message', 'Unknown error')
        return render(request, 'home.html', {'error_message': error_message})

def historical_weather(request, city, date):
    historical_weather_url = f"{HISTORICAL_WEATHER_API_URL}?key={WEATHER_API_KEY}&q={city}&dt={date}"
    response = requests.get(historical_weather_url)
    data = response.json()

    if response.status_code == 200:
        return render(request, 'historical_weather.html', {'city': city, 'weather_data': data})
    else:
        error_message = data.get('error', {}).get('message', 'Unknown error')
        return render(request, 'home.html', {'error_message': error_message})
