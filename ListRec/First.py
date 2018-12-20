List = [3, 7, 7, 4, 6, 1, 12, 10, 0, 7, 7, 9]
print(List)

suma = 0 #for
for i in List:
	suma += i
print("Цикл for: ", suma)

i = 0 #while
suma = 0
while i < len(List):
	suma += List[i]
	i += 1
print("Цикл while: ", suma)

def suma(numbers): #рекурсія без збереження даних
	if len(numbers) == 1:
		return numbers[0]
	else:
		return numbers[0] + suma(numbers[1:])
print("Рекурсія без збереження даних: ", suma(List))

def ak_suma(numbers, step = 0):
	if step == len(numbers):
		return 0
	return numbers[step] + ak_suma(numbers, step + 1)
print("Акумуляторна рекурсія: ", ak_suma(List))