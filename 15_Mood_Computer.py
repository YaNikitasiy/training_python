# Компьютерный датчик настроения
# Демонстрирует использование elif
import random

print("Я ощущаю вашу энергетику. От моего экрана не скрыто ни одно из ваших чувств.")
print("Итак, ваше настроение...")
mood = random.randint(1, 3)
if mood == 1:
    #Радостное
    print( \
        """
        ________________
       |                | 
       |   0         0  |
       |                |
       |        <       |
       |                |
       |   .        .   |
       |    '......'    |
       |________________|  
                        """)
elif mood == 2:
    #Так себе
    print( \
        """
        ________________
       |                | 
       |   0         0  |
       |                |
       |        <       |
       |                |
       |   ..........   |
       |                |
       |________________|  
                        """)
elif mood == 3:
    # прескверно
    print( \
        """
        ________________
       |                | 
       |   0         0  |
       |                |
       |        <       |
       |                |
       |      . ' .     |
       |     '     '    |
       |________________|  
                        """)
else:
    print('Не бывает такого настроения! (Должно быть, вы совершенно не в себе)')
print('....Но это только сегодня.')
input("\n\nНажмите Enter, чтобы выйти.")