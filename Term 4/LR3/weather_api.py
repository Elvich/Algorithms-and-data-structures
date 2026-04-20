import requests

def get_weather(city_name):
    """Возвращает температуру и описание погоды по названию города."""
    api_key = "FAKE_API_KEY"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        temp = data['current']['temp_c']
        desc = data['current']['condition']['text']
        
        return {"temp": temp, "desc": desc}
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            raise ValueError(f"Город '{city_name}' не найден.")
        return None
    except Exception:
        return None
