print ("Перше завдання, перший варіант")
a = float (input("Катет = ")) #користувач вводить довжини сторін
b = float (input("Катет = "))
c = float (input("Гіпотенуза = "))
if c**2 == (a**2 + b**2): #теорема Піфагора
	l = sorted ([a, b, c], reverse = True)
	print("Трикутник прямокутний, сторони у порядку спадання:", l)
else:
	print("Трикутник не прямокутний")
