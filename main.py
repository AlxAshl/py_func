#Функции: четное-нечетное и суммы

#Четное-нечетное
number = int(input("Введите число: "))
if number % 2 == 0:
    print("Число четное.")
else:
    print("Число нечетное.")

#Сумма
def sum_list(numbers):
    return sum(numbers)

print(sum_list([1, 2, 3, 4, 5]))
