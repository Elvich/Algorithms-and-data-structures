import requests
from bs4 import BeautifulSoup
import concurrent.futures
import time
import json

# Задание 1: Выбор целевых URL
URLS = [
    "https://ru.wikipedia.org/wiki/Python",
    "https://ru.wikipedia.org/wiki/Веб-скрейпинг",
    "https://ru.wikipedia.org/wiki/Поисковый_робот",
    "https://ru.wikipedia.org/wiki/Многопоточность",
    "https://ru.wikipedia.org/wiki/Параллельные_вычисления",
    "https://ru.wikipedia.org/wiki/HTML",
    "https://ru.wikipedia.org/wiki/HTTP",
    "https://ru.wikipedia.org/wiki/Transmission_Control_Protocol",
    "https://ru.wikipedia.org/wiki/UDP",
    "https://ru.wikipedia.org/wiki/Сокет_(программный_интерфейс)",
]


# Задание 2: Функция парсинга
def parse_page(url):
    """
    Парсит содержимое страницы по заданному URL.

    Извлекает заголовок H1 и первые три абзаца текста со страницы.

    Args:
        url (str): URL-адрес страницы для парсинга.

    Returns:
        dict: Словарь с результатами, содержащий 'url', 'title' и
            'content' или 'error' в случае неудачи.
    """
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36"
            )
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        title_element = soup.find("h1")
        if title_element:
            title = title_element.text.strip()
        else:
            title = "Заголовок не найден"

        paragraphs = soup.find_all("p")
        text_content = []
        for p in paragraphs:
            text = p.text.strip()
            if text:
                text_content.append(text)
                if len(text_content) >= 3:
                    break

        return {"url": url, "title": title, "content": text_content}

    except requests.exceptions.RequestException as e:
        print(f"Ошибка сети при запросе {url}: {e}")
        return {"url": url, "error": str(e)}
    except AttributeError as e:
        print(f"Ошибка извлечения данных на {url}: {e}")
        return {"url": url, "error": str(e)}
    except Exception as e:
        print(f"Неизвестная ошибка на {url}: {e}")
        return {"url": url, "error": str(e)}


def run_single_thread(urls):
    """
    Выполняет парсинг списка URL в однопоточном режиме.

    Args:
        urls (list[str]): Список URL-адресов для обработки.

    Returns:
        list[dict]: Список словарей с результатами парсинга каждой страницы.
    """
    start_time = time.time()
    results = []
    for url in urls:
        results.append(parse_page(url))
    end_time = time.time()
    elapsed = end_time - start_time
    print(f"Время выполнения (однопоточный режим): {elapsed:.4f} сек")
    return results


# Задание 3: Многопоточная обработка
def run_multi_thread(urls, max_workers=5):
    """
    Выполняет парсинг списка URL в многопоточном режиме.

    Args:
        urls (list[str]): Список URL-адресов для обработки.
        max_workers (int, optional): Максимальное количество потоков.
            По умолчанию равно 5.

    Returns:
        list[dict]: Список словарей с результатами парсинга каждой страницы.
    """
    start_time = time.time()
    results = []
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=max_workers
    ) as executor:
        for result in executor.map(parse_page, urls):
            results.append(result)
    end_time = time.time()
    elapsed = end_time - start_time
    # Задание 5: Измерение производительности
    print(
        f"Время выполнения (многопоточный режим, {max_workers} потоков): "
        f"{elapsed:.4f} сек"
    )
    return results


print(f"Запуск парсинга для {len(URLS)} URL...\n")

print("--- Однопоточный режим ---")
results_single = run_single_thread(URLS)

print("\n--- Многопоточный режим ---")
results_multi = run_multi_thread(URLS, max_workers=5)

output_file = "scraping_results.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results_multi, f, ensure_ascii=False, indent=4)

print(f"\nДанные успешно сохранены в файл: {output_file}")
