import random as ran
# пишем сортировку выбором для урпорядочивания массива
list_1 = []
sorted_list = []
counter_1 = 0
counter_2 = 0
for i in range(1, 101):
    list_1.append(ran.randint(1, 1000000))
while len(list_1) > 0:
    min = list_1[0]
    for i in range (0, len(list_1)):
        if list_1[i] < min:
            min = list_1[i]
    sorted_list.append(min)
    list_1.remove(min)
print(sorted_list)
chosen = input("Введите элемент, который хотите найти\n")
# проводим линейный поиск
for i in range(1, len(sorted_list)+1):
    counter_1 += 1
    if sorted_list[i-1] == int(chosen): # сравниваем элемент списка с искомым
        print("Элемент найден в позиции", i)
        print("В линейном поиске было проведено", counter_1, "сравнений")
# вводим начало, конец и середину списка
first = 0
last = len(sorted_list) - 1
central = len(sorted_list) // 2
while first <= last:
    if int(chosen) == sorted_list[central]:
        print("В бинарном поиске было проведено", counter_2, "сравнений")
        break
    # обрезаем массив исходя из сравнения нужного элемента с центральным
    if int(chosen) > sorted_list[central]:
        first = central + 1
    else:
        last = central - 1
    central = (first + last) // 2
    counter_2 += 1
else:
    print("Элемент не найден")    