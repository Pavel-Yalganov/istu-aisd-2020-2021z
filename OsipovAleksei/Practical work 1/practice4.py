#Разработайте следующий алгоритм сортировки. Дан массив чисел от 0 до 9.
# Посчитайте кол-во повторений каждой из цифр и выведите отсортированный массив
# (упорядоченный от меньшего к большему) на основе этой информации.
arr = [1, 5, 7, 9, 0, 2, 3, 5, 5, 8, 9, 6, 8, 4, 3, 1, 2, 4, 6, 7, 8, 0]
count = [0] * 10

for i in arr:
    count[i] += 1
print (count)
#Из массива счетчика нужно создать результирующий массив

rez = []
for i in range(len(count)):
    if count[i] > 0:
        for j in range(count[i]):
            rez.append(i)

print (rez)