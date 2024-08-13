
cook_book = {}
title = ['ingredient_name', 'quantity', 'measure']
with open('recipes.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip().split(' | ')
        if len(''.join(line)) > 1:
            if len(line) == 1 and not ''.join(line).isdigit(): 
                key = line[0]
                cook_book[key] = []
            elif not ''.join(line).isdigit():
                cook_book[key].append(dict(zip(title, line)))
                
print(cook_book)