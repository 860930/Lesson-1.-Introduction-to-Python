# Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
# 20 -> Да
# 70 -> Да
# 90 -> Нет

print ('Введите число: ')
a = int(input())
if (a % 5 == 0 and a%10 == 0 or a%15 == 0) and a % 30:
 print('Да')
else:
 print('Нет')   

