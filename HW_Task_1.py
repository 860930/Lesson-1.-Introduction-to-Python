# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
#- 6 -> да
#- 7 -> да
#- 1 -> нет

print ('Введите цифру обозначающую день недели: ')
a = int(input())
if (5 < a < 8):
 print ('Да, это выходной день!')
elif (1 > a > 7):
  print ('Это не день недели!')
else:
 print ('Нет, это не выходной день!')

