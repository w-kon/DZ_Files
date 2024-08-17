
# Задача №1

def dictionary_list(list_recipes):
    cook_book = {}
    title = ['ingredient_name', 'quantity', 'measure']
    for line in list_recipes:
        line = line.strip().split(' | ')
        if len(''.join(line)) > 1:
            if len(line) == 1 and not ''.join(line).isdigit(): 
                key = line[0]
                cook_book[key] = []
            elif not ''.join(line).isdigit():
                cook_book[key].append(dict(zip(title, line)))
    return cook_book

def open_recipes():
    with open('recipes.txt', 'r', encoding='utf-8') as file:
        return(dictionary_list(file))


# Задача №2

def get_shop_list_by_dishes(dishes, person_count):
    resalt = {}
    cook_book = open_recipes()
    
    for dish in dishes:
        ingredient_list = cook_book[dish]
        for ingredient in ingredient_list:
                if ingredient['ingredient_name'] in resalt:
                    resalt[ingredient['ingredient_name']]['quantity'] = str(int(resalt[ingredient['ingredient_name']]['quantity']) + int(ingredient['quantity']) * int(person_count))
                else:
                    resalt[ingredient['ingredient_name']] = dict(measure = ingredient['measure'], quantity = str(int(ingredient['quantity']) * int(person_count)))
    return resalt
#print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2))
#get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2)
(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2))

