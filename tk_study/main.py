#b = int(input()) #школьники
#c = int(input()) #мандарины

#a = c // b
#d = c % b
#print(a)
#print(d)


#b = int(input()) #минуты

#a = b // 60 #часы
#d = b % 60  #мин
#print( str(b) + " " + "мин" + " " + '-' + " " + 'это' + " " + str(a) + " " + 'час' + " " + str(d) + " " + 'минут.')

#-----------------------------------------------

#
# n = int(input())
#
# a = n // 100          # сотни
# b = (n // 10) % 10    # десятки
# c = n % 10            # единицы
#
# sum_digits = a + b + c
# prod_digits = a * b * c

# print("Сумма цифр =", sum_digits)
# print("Произведение цифр =", prod_digits)
#---------------------------------------
# n = int(input())
#
# a = n // 100          # сотни
# b = (n // 10) % 10    # десятки
# c = n % 10            # единицы
#
# print(a, b, c, sep='')
# print(a, c, b, sep='')
# print(b, a, c, sep='')
# print(b, c, a, sep='')
# print(c, a, b, sep='')
# print(c, b, a, sep='')
#--------------------------
# n = int(input())
#
# thousands = n // 1000           # тысячи
# hundreds = (n // 100) % 10      # сотни
# tens = (n // 10) % 10           # десятки
# units = n % 10                  # единицы
#
# print("Цифра в позиции тысяч равна", thousands)
# print("Цифра в позиции сотен равна", hundreds)
# print("Цифра в позиции десятков равна", tens)
# print("Цифра в позиции единиц равна", units)
#----------------------------


# a = int(input())
# b = int(input())
# c = int(input())
#
# if b - a == c - b:
#     print("YES")
# else:
#     print("NO")
#----------------------------------

# n = int(input())
#
# # Выделяем цифры четырёхзначного числа
# thousands = n // 1000          # первая цифра (тысячи)
# hundreds = (n // 100) % 10     # вторая цифра (сотни)
# tens = (n // 10) % 10          # третья цифра (десятки)
# units = n % 10                 # четвёртая цифра (единицы)

# # Проверяем условие: сумма первой и последней = разности второй и третьей
# if thousands + units == hundreds - tens:
#     print("ДА")
# else:
#     print("НЕТ")
#----------------------
# a = int(input())
# b = int(input())
# c = int(input())
#
# sum_positive = 0
#
# if a > 0:
#     sum_positive = sum_positive + a
# if b > 0:
#     sum_positive = sum_positive + b
# if c > 0:
#     sum_positive = sum_positive + c
#
# print(sum_positive)
#-------------------------

# age = int(input())
#
# if age <= 13:
#     print("детство")
# elif age <= 24:
#     print("молодость")
# elif age <= 59:
#     print("зрелость")
# else:
#     print("старость")
#-------------------------

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# min_num = a
#
# if b < min_num:
#     min_num = b
# if c < min_num:
#     min_num = c
# if d < min_num:
#     min_num = d
#
# print(min_num)
#------------
