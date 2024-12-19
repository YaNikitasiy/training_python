# Эксклюзивная сеть
# Демонстрирует составные условия и логические операторы
print("\tЭксклюзивная компьютерная сеть")
print("\tТолько для зарегистрированных пользователей\n")
security = 0
username = ""
while not username:
    username = input("Логин: ")
password = ""
while not password:
    password = input("Пароль: ")
if username == "N.Maletina" and password == "Finik":
    print("\nПривет, Солнышко")
    security = 5 
elif username == "S.Nechaev" and password == "A gde loot?":
    print("\nВсё, давай, попу подотри")
    security = 3
elif username == "K.Litvinov" and password == "EbuForus":
    print("\nВыпьем за забор")
    security = 3
elif username == "Guest" or password == "Guest":
    print("\nНикита, хочешь расстрою?")
    security = 1
else:
    print(
        "Войти в систему не удалось. Должно быть, вы не очень-то эксклюзивный гражданин.\n"
    )
input("\n\nНажмите Enter, чтобы выйти.")