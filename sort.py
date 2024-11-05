import random as ran
# создаём два списка
list_1 = [] 
list_2 = []
counter_1 = 0
counter_2 = 0
# заполняем два списка
for i in range(1, 101):
    a = ran.randint(1, 1000000)
    list_1.append(a)
    list_2.append(a)
print(list_1)
stop_flag = False
# проводим сортировку пузырьком
while (stop_flag is False):
    stop_flag = True
    for i in range (0, len(list_1) - 1):
        # сравниваем два соседних элемента
        if list_1[i] < list_1[i+1]:
            a = list_1[i]
            list_1[i] = list_1[i+1] # заменяем элементы
            list_1[i+1] = a
            stop_flag = False
            counter_1 += 1
    print(list_1)
    # вводим пустой список для записи результатов сортировки выбором
sorted_list = []
while len(list_2) > 0:
    max = list_2[0]
    for i in range (0, len(list_2)):
        if list_2[i] > max:
            max = list_2[i] # вставляем элемент в пустой список
    sorted_list.append(max)
    list_2.remove(max)
    counter_2 += 1
    print(sorted_list)
print(sorted_list)  
print("В сортировке пузырьком было", counter_1, "итераций")
print("В сортировке выбором было", counter_2, "итераций")