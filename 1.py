n = int(input("Введіть довжину масиву: "))

arr = []
for i in range(n):
    element = float(input(f"Введіть елемент {i+1}: "))
    arr.append(element)

positive_elements = [x for x in arr if x > 0]
print("Додатні елементи у зворотному порядку:", positive_elements[::-1])
