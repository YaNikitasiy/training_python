# Задание_5
# Напишите программу - симулятор пирожка с "сюрпризом", - которая бы при запуске отображала один из пяти различных
# "сюрпризов", выбранный случайным образом

print(
    "Добрый день, в нашем заведении вы не выбираете еду, вы либо берете пирожок с сюрпризом, либо нет"
)
print("Кроме таких пирожков у нас нихрена нет, так что давайте подберем вам")
che = ""
while che != "да":
    che = input("Хотите пирожок? ")
    print("Тогда иди ка ты нахуй")
import random

piroshok = random.randint(1, 5)

if piroshok == 1:
    print("\nКОЗЮЛЬКИ!\n")
    print("О, фартануло, пирожок с козюльками")
elif piroshok == 2:
    print("\nПАРАША!\n")
    print("Ну хз хз, пирожок с парашей мало кому по душе")
elif piroshok == 3:
    print("\nПУКАЧИ\n")
    print("Мммм, ну делисиосо")
elif piroshok == 4:
    print("\nЧеркаши\n")
    print("Сююююдааа, мое любимое")
elif piroshok == 5:
    print("\nКакашки Финика\n")
    print("Фирменный рецепт")
    
