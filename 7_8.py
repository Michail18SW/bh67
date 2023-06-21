def find_country(cities, city):
    for country, city_list in cities.items():
        if city in city_list:
            return country
    return "Город не найден"

cities = {
    "Россия": ["Москва", "Санкт-Петербург", "Казань"],
    "Беларусь": ["Минск", "Гомель", "Витебск", "Гродно"],
    "Украина": ["Киев", "Одесса", "Херсон", "Донецк"],
    "Франция": ["Париж", "Марсель", "Лион"],
    "Италия": ["Рим", "Милан", "Венеция"],
}

city = input("Введите город: ")
country = find_country(cities, city)
if country == "Город не найден":
    print(country)
else:
    print(f"{city} находиться в стране под названием {country}")
