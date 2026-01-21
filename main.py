from http_client import get


def show_raw_json():
    """Пункт меню 1: сделать GET-запрос и показать сырой JSON."""
    url = input("Введите URL: ").strip()
    if not url:
        print("URL не может быть пустым!")
        return
    
    result = get(url)
    if result:
        print("\nРезультат:")
        print(result)
    print()


def country_info():
    """Пункт меню 2: информация о стране через Rest Countries API."""
    country_name = input("Введите название страны: ").strip()
    if not country_name:
        print("Название страны не может быть пустым!")
        return
    
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    result = get(url)
    
    if result:
        # API возвращает список стран, берем первую
        if isinstance(result, list) and len(result) > 0:
            country = result[0]
            name = country.get("name", {}).get("common", "Неизвестно")
            capital = country.get("capital", ["Неизвестно"])[0] if country.get("capital") else "Неизвестно"
            population = country.get("population", "Неизвестно")
            
            print("\nИнформация о стране:")
            print(f"Название: {name}")
            print(f"Столица: {capital}")
            print(f"Население: {population}")
        else:
            print("Страна не найдена.")
    print()


def random_dog():
    """Пункт меню 3: получить случайную картинку собаки."""
    url = "https://dog.ceo/api/breeds/image/random"
    result = get(url)
    
    if result:
        image_url = result.get("message")
        if image_url:
            print(f"\nСсылка на картинку: {image_url}")
        else:
            print("Не удалось получить ссылку на картинку.")
    print()


def main():
    """Главная функция с консольным меню."""
    while True:
        print("=" * 50)
        print("Меню:")
        print("1 — Сделать GET-запрос по URL (показать сырой JSON)")
        print("2 — Информация о стране (Rest Countries)")
        print("3 — Случайная собака (Dog API)")
        print("0 — Выход")
        print("=" * 50)
        
        choice = input("Выберите пункт меню: ").strip()
        
        if choice == "1":
            show_raw_json()
        elif choice == "2":
            country_info()
        elif choice == "3":
            random_dog()
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.\n")


if __name__ == "__main__":
    main()
