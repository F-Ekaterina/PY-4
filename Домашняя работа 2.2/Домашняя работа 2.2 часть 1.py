import json
from pprint import pprint


def get_cook_book():
    with open ('cook_book_for_2.2.json', encoding='utf8') as f:
        cook_book=json.load(f)
        pprint(cook_book)
    return cook_book

def get_shop_list_by_dishes(person_count, dishes):
    cook_book = get_cook_book()
    print(cook_book)
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

