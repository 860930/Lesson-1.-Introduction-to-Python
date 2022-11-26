# Вывести на экран числа от -N до N
# 5 -> -5,-4,-3,-2,-1,0,1,2,3,4,5

print ('Введите целое число a: ')
a = int(input())
if a > 0:
    print(*range(-a,a+1))
else:
    print(*range(-a,a-1,-1))