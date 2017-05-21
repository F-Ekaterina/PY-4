Домашняя работа 1.1 часть 2
print ('"ремонт"')
room_area1=14.4#m2
room_area2=8.8#m2

flooring_1=1000#rub/m2
flooring_2=3500#rub/m2
print ('цена м2 напольного покрытия 1', flooring_1, 'руб')
print ('цена м2 напольного покрытия 2', flooring_2, 'руб')

option_1=(room_area1+room_area2)*flooring_2
option_2=room_area1*flooring_1+room_area2*flooring_2
option_3=(room_area1+room_area2)*flooring_1

budget_floor=40000#rub
print ('бюджет на ремонт пола',budget_floor)

if budget_floor>option_1:
  proficit=budget_floor-option_1
  print ('делаем вариант 1', 'остаток',proficit, 'руб')
else:
    print ('проверяем вариант 2->')
if budget_floor>option_2:
  proficit=budget_floor-option_2
  print ('делаем вариант 2','остаток',proficit, 'руб')
else:
  print ('проверяем вариант 3->')
if budget_floor>option_3:
  proficit=budget_floor-option_3
  print ('делаем вариант 3','остаток',proficit, 'руб')
else:
  print ('копим деньги')