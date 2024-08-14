
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

with open('recipes.txt', 'r', encoding='utf-8') as file:
    print(dictionary_list(file))




