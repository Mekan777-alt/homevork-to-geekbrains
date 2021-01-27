# Создаем 4 переменные со значениями словарями
account1 = {'login': 'ivan', 'password': 'q1'} 
account2 = {'login': 'petr', 'password': 'q2'} 
account3 = {'login': 'olga', 'password': 'q3'} 
account4 = {'login': 'anna', 'password': 'q4'} 
# Создаем 4 переменные так же со значениями словарями то что в кавычках это ключ ко словорям
user1 = {'name': 'Иван', 'age': '20', 'account': account1}
user2 = {'name': 'Петр', 'age': '25', 'account': account2}
user3 = {'name': 'Ольга', 'age': '18', 'account': account3}
user4 = {'name': 'Анна', 'age': '27', 'account': account4}
# Создаем список состоящий из всех узеров
user_list = ['user1', 'user2', 'user3', 'user4']
# Создаем переменную где будет спрашиваться у юзера что надо ввести
users = str(input('Введите ключ (name или account)' ))
# Обработка исключений
try:
    print(f"Значения ключа name для юзера 1 = {user1['name']}")
    print(f"Значения ключа name для юзера 2 = {user2['name']}")
    print(f"Значения ключа name для юзера 3 = {user3['name']}")
    print(f"Значения ключа name для юзера 4 = {user4['name']}")
except KeyError:
    print("Ключ не найден")

user_number = int(input('Введите порядковый номер: '))
user = user_list[int(user_number)-1]
try:
    print(f"Данные по юзеру № {user_number}")
    print(f"Имя: {user['name']}")
    print(f"Возраст: {user['age']}")
    print(f"Логин: {account['login']}")
    print(f"Пароль: {account['password']}")
except TypeError:
    print("Пользователь не найден")





