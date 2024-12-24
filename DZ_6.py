# Задание_6
# Напишите программу которая "подбрасывала" условную монету 100 раз и сообщала, сколько раз выпал орел, а сколько - решка

import random

total = 0
orel = 1
reshka = 1

while total < 98:
    token = random.randint(0, 1)
    if token == 1:
        total += 1
        orel += 1
    if token == 0:
        total += 1
        reshka += 1

print("Орел выпал ровно ", orel, "раз")
print("Решка выпала ровно" , reshka, "раз")
