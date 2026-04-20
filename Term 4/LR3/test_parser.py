from unittest.mock import patch, Mock
from parser import extract_paragraphs

@patch('parser.requests.get')
def test_extract_paragraphs_success(mock_get):
    # Создаем фиктивный ответ
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = "<html><body><p>Первый абзац</p><p>Второй абзац</p><p></p></body></html>"
    mock_get.return_value = mock_response

    result = extract_paragraphs("http://test-site.ru")
    
    # Проверяем, что запрос был вызван с правильным URL
    mock_get.assert_called_once_with("http://test-site.ru", timeout=5)
    
    # Проверяем результат парсинга (игнорируются пустые абзацы)
    assert len(result) == 2
    assert result[0] == "Первый абзац"
    assert result[1] == "Второй абзац"

@patch('parser.requests.get')
def test_extract_paragraphs_empty(mock_get):
    # Страница без параграфов
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = "<html><body><h1>Только заголовок</h1></body></html>"
    mock_get.return_value = mock_response

    result = extract_paragraphs("http://test-site.ru")
    assert isinstance(result, list)
    assert len(result) == 0

@patch('parser.requests.get')
def test_extract_paragraphs_error(mock_get):
    # Имитация ошибки сети (Exception)
    mock_get.side_effect = Exception("Сетевая ошибка")
    
    result = extract_paragraphs("http://error-site.ru")
    assert isinstance(result, list)
    assert len(result) == 0
