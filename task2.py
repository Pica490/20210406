with open('recipes.txt', 'r', encoding = 'utf-8') as f:

    def get_shop_list_by_dishes(dishes, person_count):
        shopping_list = {}
        list_recipes = f.readlines()
        for dish in dishes:
            g = 0
            if dish+"\n" in list_recipes:
                for line in list_recipes:
                    g += 1
                    if dish == line.strip():
                        number_str = int(list_recipes[g])
                        i = 1
                        for i in range(number_str):
                            ingredient_name, quantity, measure = list_recipes[g+1+i].strip().split('|')
                            if ingredient_name not in shopping_list:
                                shopping_list[ingredient_name] = {'quantity': int(quantity)*person_count, 'measure': measure}
                            else:
                                current_s_l = shopping_list[ingredient_name]
                                new_quantity = int(current_s_l['quantity']) + int(quantity)*person_count
                                shopping_list[ingredient_name] = {'quantity': new_quantity,'measure': measure}
            else:
                print(f'{dish} в книге рецептов нет!')

        return shopping_list

    print(get_shop_list_by_dishes(['Фахитос', 'Борщ'],2))