import requests


def get(url, params=None, timeout=10):
    """
    Отправляет GET-запрос по указанному URL.
    
    Args:
        url: URL для запроса
        params: словарь с параметрами запроса (опционально)
        timeout: таймаут запроса в секундах (по умолчанию 10)
    
    Returns:
        dict: JSON-ответ, если статус 200
        None: в случае ошибки
    """
    try:
        response = requests.get(url, params=params, timeout=timeout)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Ошибка: статус {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Ошибка сети: {e}")
        return None
