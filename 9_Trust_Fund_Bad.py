# Рантье (версия с ошибкой)
# Демонстрирует логическую ошибку
print(
    """
\t\t Рантье
Программа подсчитывает ваши ежемесячные расходы. Эту статистику нужно знать затем,
чтобы у вас не закончились деньги и вам не пришлось искать работу.
Введите суммы расходов по всем статьям, перечисляемым ниже. Вы - богаты
так и не мелочитесь, пишите суммы в долларах, без центов""")
car = input('Техническое обслуживание машины "Ламборгини": ')
rent = input('Съем роскошной квартиры на Манхэттене: ')
jet = input('Аренда самолета: ')
gifts = input('Подарки: ')
food = input('Обеды и ужины в ресторанах: ')
staff = input('Зарплата прислуги: ')
guru = input('Оплата психолога: ')
games = input('донаты в Доточку: ')
total = car + rent + jet + gifts + food + staff + guru + games
print('\nОбщая сумма.', total)
input('\n\nНажмите Enter, чтобы выйти')