import os
def read_cook_book():
    file_path = os.path.join(os.getcwd(), 'cook_book.txt')
    cook_book = {}

    f = open('cook_book.txt')

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            dish = line.strip()
            count_ingr = int(f.readline())
            list_ingr = list()
            for item in range(count_ingr):
                ingrs = {}
                ingr = f.readline().strip()
                ingrs['ingredient_name'], ingrs['quantity'], ingrs['measure'] = ingr.split('|')
                ingrs['quantity'] = int(ingrs['quantity'])
                list_ingr.append(ingrs)
            f.readline()
        cook_book[dish] = list.ingr
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    list_ingr = dict()

    for dish in dishes:
        if dish in read_cook_book():
            for ingrs in read_cook_book()[dish]:
                mq_list = dict()
                if ingrs['ingredient_name'] not in list_ingr:
                    mq_list['measure'] = ingrs['measure']
                    mq_list['quantity'] = ingrs['quantity'] * person_count
                    list_ingr[ingrs['ingredient_name']] = mq_list
                else:
                    list_ingr[ingrs['ingredient_name']]['quantity'] = \
                    list_ingr[ingrs['ingredient_name']]['quantity'] + ingrs['quantity'] * person_count
        else:
            return 'Null'
    return list_ingr