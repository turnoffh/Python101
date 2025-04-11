lives = 3
print(type(lives))
age = 12
budget = 100
temperature = 12.12
print(type(temperature))
lives = 2
print(lives)
lives = 1
print(lives)
lives = 12 + 15
print(lives)
lives = lives - 1
print(lives)
lives -= 1
print(lives)
lives -= 5
print(lives)
lives += 5
print(lives)
number = 4500000000000000000.1 #Notacion cientifica
print(number)
number_b = 0.0000000000000001 #Notacion cientifica
print(number_b)
# Presupuesto de 3 meses
budget_january = input("¿Cuál es tu presupuesto para Enero?")
budget_february = input("¿Cuál es tu presupuesto para Febrero?")
budget_march = input("¿Cuál es tu presupuesto para Marzo?")
budget_total = int(budget_january) + int(budget_february) + int(budget_march)
print("El presupuesto total es: ", budget_total)
print("El promedio es: ", budget_total / 3)
