users = {
    1: {"first_name": "Михаил", "last_name": "Скрипка", "phone": "+375441234567", "email": ""},
    2: {"first_name": "Моисей", "last_name": "Сергеев", "phone": "+375447654321", "email": "maisey@mail.ru"},
    3: {"first_name": "Лилия", "last_name": "Цветкова", "phone": "+375440001122"}
    }

for user_id, user_data in users.items():
    if not user_data.get('email'):
        print(user_data['first_name'])
