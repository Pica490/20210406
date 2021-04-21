with open('recipes.txt', 'r', encoding = 'utf-8') as f:
    cook_book = {}
    for line in f:
        list_ingr = []
        head_dict = line.strip()
        number_str = int(f.readline())
        cook_book[head_dict] = list_ingr
        i=1
        for i in range(number_str):
            ingredient_name, quantity, measure = f.readline().strip().split('|')
            list_ingr.append({'ingredient_name': ingredient_name,'quantity': quantity, 'measure': measure})
        f.readline()

    for key, value in cook_book.items():
        print (key)
        for v in value:
            print(v)

    def get_shop_list_by_dishes(dishes, person_count):
        shopping_list = {}
        for dish in dishes:
            if dish in cook_book:
                for ingr in cook_book[dish]:
                    if ingr['ingredient_name'] not in shopping_list:
                        shopping_list[ingr['ingredient_name']] = {'quantity': int(ingr['quantity'])*person_count, 'measure': ingr['measure']}
                    else:
                        current_s_l = shopping_list[ingr['ingredient_name']]
                        new_quantity = int(current_s_l['quantity']) + int(ingr['quantity'])*person_count
                        shopping_list[ingr['ingredient_name']] = {'quantity': new_quantity, 'measure': ingr['measure']}
            else:
                print(f'{dish} в книге рецептов нет!')
        return shopping_list

    print(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'],1))

