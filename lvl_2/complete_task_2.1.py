# Задача 2.1.

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

arr=[4,6,2,1,9,63,-134,566]

def minimum(arr):
    min_number = arr[0]
    for i in arr[1:]:
        if i < min_number:
            min_number = i
    return min_number

def maximum(arr):
    max_number = arr[0]
    for j in arr[1:]:
        if j > max_number:
            max_number = j
    return max_number

# print(f'Месяц {month} ({(datetime.date(1, month, 1)).strftime("%B")}) является частью {ochered[math.ceil(month/3)]} квартала')
print(f'arr= {arr} " -> min = " {minimum(arr)} " , max = " {maximum(arr)}')
