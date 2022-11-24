# Найти максимальное из пяти чисел
# 1,4,8,7,5 -> 8
# 78,55,36,90,2 -> 90

print ('Введите числа: ')
num_max = 0
for i in range(5):
    a = int(input())
    if a > num_max:
     num_max = a

print ("max=" , num_max)
