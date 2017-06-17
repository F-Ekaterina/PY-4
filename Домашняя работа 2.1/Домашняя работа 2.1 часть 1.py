#with open ('cook_book.txt', encoding='utf8') as f:
#    print(f.readlie())
#    dishes=[]
#    for  line in f:
#        print(line)
#        dishes.append(line.strip())
    #print(dishes)
#    f.close()
#for el in dishes:
#    if '' in dishes:
#        dishes.remove('')
       # print(dishes)
#dish_1=dishes[0]
#print(dish_1)
#a=int(dishes[1]) #=2
#print(a)
#b=dishes[2:2+a]
#print(b)
#dish_2=dishes[2+a]
#print(dish_2)
#c=int(dishes[2+a+1])#=5
#print(c)
#d=dishes[a+3+1:a+3+1+c]
#print(d)
#dish_3=dishes[a+3+1+c]
#print(dish_3)
#e=int(dishes[a+4+c+1]) #=12
#print(e)
#g=dishes[a+5+c+1:a+5+c+1+e]
#print(g)
#print("____________", "\n")

#for ingredient_b in b:
#    dish_1_list = []
#    dish_1_list.append(ingredient_b.split('|'))
#    print(dish_1_list)
#    print('\n')

#for ingredient_d in d:
#    dish_2_list = []
#    print(ingredient_d.split('|'))
#    print(ingredient_d.replace('|', ','))
#    dish_2_list.append(ingredient_d)
#    print(dish_2_list)
#    print('\n')

#for ingredient_g in g:
#    dish_3_list = []
#    print(ingredient_g.split('|'))
#    print(ingredient_g.replace('|', ','))
#    dish_3_list.append(ingredient_g)
#    print(dish_3_list)
#    print('\n')

#ingredient_dishes=[dish_1_list, dish_2_list, dish_3_list]
#print(ingredient_dishes)

def get_cook_book():
    with open('cook_book.txt', encoding='utf8') as f:
        line=f.readline() #1cтрока
        cook_book = {}  # создаем пустой словарь
        # print(line)
        while line:
            while len(line.strip())==0: #если строка пустая, читаем следующую строку
                line=f.readline()
               # print(line)
            key_dish=line.strip().lower() #так как в следующей строке название, объявляем ее ключом
            dish_list=[] #создаем пустой список
            quantity_ingridients=int(f.readline()) # читаем следующую строку.
                                                    # так как там находится значение сколько строк нам нужно
                                                   # переводим строку в числовое значение
            for element in range(0,quantity_ingridients): #для элементов в интервале от 0 до числа,
                                                          # указанного в quantity_ingridients
                ingridient_values=f.readline().strip().split('|') # для key_dish читаем следующие строки вида а/б/в,
                                                                  # обрезаем края, делим по '|'
                dish_dict={                                       #создаем словарь с ингридиентами блюда
                    'ingridient_name' : ingridient_values[0],
                    'quantity' : int(ingridient_values[1]),
                    'measure' : ingridient_values [2]
                }
                #print(dish_dict)
                dish_list.append(dish_dict)                 #запихиваем полученный словарь в ранее созданный список

            #print(dish_list, '\n')
            #cook_book={
            #    key_dish : dish_list
            #}                                              #соотносим ключ со значением в ранее созданном словаре

            cook_book[key_dish]=dish_list
            #print(cook_book)
            line=f.readline()                               #читаем следующую строку
        return cook_book

#get_cook_book()




def get_shop_list_by_dishes(person_count, dishes):
    cook_book = get_cook_book()
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            #print(new_shop_list_item)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))


def create_shop_list():
    person_count = int(input('Введите количество человек'))
    dishes = input('Введите наименования блюд в расчете на одного (через запятую)').lower().split(', ')
    shop_list = get_shop_list_by_dishes(person_count, dishes)
    print_shop_list(shop_list)


create_shop_list()

