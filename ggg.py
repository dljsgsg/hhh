#1
# Создать четыре списка целых
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
list3 = [11, 13, 15, 17, 19]
list4 = [12, 14, 16, 18, 20]

# Объединить списки в пятом списке
combined_list = list1 + list2 + list3 + list4

# Получить выбор пользователя для сортировки
sort_choice = input("Сортировать по убыванию (1) или возрастанию (2)? ")

# Сортировать по выбору пользователя
if sort_choice == "1":
    combined_list.sort(reverse=True)
else:
    combined_list.sort()

# Найти значение, введенное пользователем, с помощью линейного поиска
user_input = int(input("Введите значение для поиска: "))
found = False
for item in combined_list:
    if item == user_input:
        found = True
        break

# Вывести результат
if found:
    print("Значение найдено в списке.")
else:
    print("Значение не найдено в списке.")
    #2
# Создать четыре списка целых
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
list3 = [11, 13, 15, 17, 19]
list4 = [12, 14, 16, 18, 20]

# Найти уникальные элементы для каждого списка
unique_elements = []
for item in list1:
    if item not in list2 and item not in list3 and item not in list4:
        unique_elements.append(item)
for item in list2:
    if item not in list1 and item not in list3 and item not in list4:
        unique_elements.append(item)
for item in list3:
    if item not in list1 and item not in list2 and item not in list4:
        unique_elements.append(item)
for item in list4:
    if item not in list1 and item not in list2 and item not in list3:
        unique_elements.append(item)

# Получить выбор пользователя для сортировки
sort_choice = input("Сортировать по убыванию (1) или возрастанию (2)? ")

# Сортировать по выбору пользователя
if sort_choice == "1":
    unique_elements.sort(reverse=True)
else:
    unique_elements.sort()

# Найти значение, введенное пользователем, с помощью бинарного поиска
user_input = int(input("Введите значение для поиска: "))
left = 0
right = len(unique_elements) - 1
found = False

while left <= right:
    mid = (left + right) // 2
    if unique_elements[mid] == user_input:
        found = True
        break
    elif unique_elements[mid] < user_input:
        left = mid + 1
    else:
        right = mid - 1

# Вывести результат
if found:
    print("Значение найдено в списке.")
else:
    print("Значение не найдено в списке.")