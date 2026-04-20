import pytest
from unittest.mock import patch, Mock
import requests
from weather_api import get_weather

@patch('weather_api.requests.get')
def test_get_weather_success(mock_get):
    # Фиктивный ответ с погодой
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "current": {
            "temp_c": 21.5,
            "condition": {"text": "Солнечно"}
        }
    }
    mock_get.return_value = mock_response

    result = get_weather("Москва")
    assert result is not None
    assert result["temp"] == 21.5
    assert result["desc"] == "Солнечно"
    mock_get.assert_called_once()

@patch('weather_api.requests.get')
def test_get_weather_city_not_found(mock_get):
    # Имитация 404 Not Found
    mock_response = Mock()
    mock_response.status_code = 404
    
    # raise_for_status должен бросать HTTPError
    error = requests.exceptions.HTTPError("404 Not Found", response=mock_response)
    mock_response.raise_for_status.side_effect = error
    mock_get.return_value = mock_response
    
    # Проверяем, что выбрасывается специфическое исключение (ValueError)
    with pytest.raises(ValueError, match="Город 'НеизвестныйГород' не найден."):
        get_weather("НеизвестныйГород")

@patch('weather_api.requests.get')
def test_get_weather_network_error(mock_get):
    # Имитация ошибки сети
    mock_get.side_effect = requests.exceptions.ConnectionError("Timeout")
    
    # При любых других ошибках возвращаем None
    result = get_weather("Санкт-Петербург")
    assert result is None
