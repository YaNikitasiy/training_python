car = int(input("Укажите стоимость автомобиля "))
nalog = car // 100 * 10
registr = car // 100 * 15
agent = 20000
dostavka = 50000
total = car + nalog + registr + agent + dostavka
print("\nОбщая стоимость покупки составит", total, "рублей")
