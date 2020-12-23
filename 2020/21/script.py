
def findSolution():
    for allergen in restrictions:
        n_foods = len(restrictions[allergen])
        if n_foods == 1:
            n_options = len(restrictions[allergen][0])
            if n_options == 1:
                return allergen, restrictions[allergen][0][0]
        else:
            ingredients_in_n_foods = dict()
            first_food = restrictions[allergen][0]
            for i in range(len(first_food)):
                ingredient = first_food[i]
                n_food = 1
                for j in range(1, n_foods):
                    food = restrictions[allergen][j]
                    if ingredient in food:
                        n_food += 1
                ingredients_in_n_foods[ingredient] = n_food
            options = dict()
            for (key, value) in ingredients_in_n_foods.items():
                if value == n_foods:
                    options[key] = value
            if len(options) == 1:
                return allergen, list(options.keys())[0]

def removeRestrictions(ingredient, allergen):
    del restrictions[allergen]
    for current_allergen in restrictions:
            n_foods = len(restrictions[current_allergen])
            for i in range(n_foods):
                if ingredient in restrictions[current_allergen][i]:
                    restrictions[current_allergen][i].remove(ingredient)


if __name__ == '__main__':
    input_file = open("2020/21/input")
    raw_lines = input_file.readlines()

    raw_lines = '''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)'''.solutionsplit('\n')

    restrictions = dict()

    all_ingredients = dict()
    line = raw_lines[0]
    for line in raw_lines:
        parts = line.strip().split('contains')
        ingredients = parts[0].split(' ')[:-1]
        for ingredient in ingredients:
            if ingredient in all_ingredients:
                all_ingredients[ingredient] += 1
            else:
                all_ingredients[ingredient] = 1
        allergens = parts[1][1:-1].split(', ')
        for allergen in allergens:
            if allergen in restrictions:
                restrictions[allergen].append(ingredients)
            else:
                restrictions[allergen] = [ingredients]

    solution = dict()
    while len(restrictions) > 0:
        allergen, ingredient = findSolution()
        solution[allergen] = ingredient
        removeRestrictions(ingredient, allergen)

    for ingredient in solution.values():
        del all_ingredients[ingredient]
    print(sum(all_ingredients.values()))

    sorted_allergen = list(solution.keys())
    sorted_allergen.sort()
    sorted_allergen

    result = []
    for key in sorted_allergen:
        result.append(solution[key])
    print(",".join(result))