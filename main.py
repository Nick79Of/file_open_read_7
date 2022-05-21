from pprint import pprint
import os

file_name = 'recipes.txt'

PATH = os.getcwd()
DIR = os.path.join(PATH, 'texts')
FILES_LST = os.listdir(DIR)


def recipes_dict(recipes):
    with open(recipes, encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            dish = line.strip()
            cook_book[dish] = []
            item_quantity = int(f.readline().strip())
            for i in range(item_quantity):
                ingredient_name, quantity, measure = map(str.strip, f.readline().split('|'))
                cook_book[dish].append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
            f.readline().strip()

        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredients in cook_book[dish]:
                ingredient, quantity, measure = ingredients
                if ingredients[ingredient] in shop_list:
                    shop_list[ingredients[ingredient]]['quantity'] += ingredients[quantity]*person_count
                else:
                    shop_list[ingredients[ingredient]] = {'measure': ingredients[measure], 'quantity': ingredients[quantity]*person_count}
        else:
            print(f'"{dish}" отсутствует в книге рецептов.')
    return shop_list


cook_book = recipes_dict(file_name)
pprint(cook_book)
shop_list = get_shop_list_by_dishes(['Омлет', 'Омлет'], 1)
pprint(shop_list)

def add_files(FILES_LST):
    files_comb = []
    for i in FILES_LST:
        with open(os.path.join(DIR, i), mode='r', encoding='utf-8') as f:
            files_comb.append((i, len(f.readlines())))
    files_comb.sort(key=lambda x: x[1])
    f = open('result.txt', 'w', encoding='utf-8')
    for name, lenght in files_comb:
        with open(os.path.join(DIR, name), mode='r', encoding='utf-8') as work_file:
            print(name + '\n' + str(lenght), file=f)
            for line in work_file:
                print(line.rstrip(), file=f)
    f.close()

add_files(FILES_LST)