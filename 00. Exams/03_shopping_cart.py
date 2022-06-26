def shopping_cart(*args):
    meal1 = 'Soup'
    meal2 = 'Pizza'
    meal3 = 'Dessert'

    meals_types = {
        meal1: (3, []),
        meal2: (4, []),
        meal3: (2, [])
    }
    for arg in args:
        if arg == 'Stop':
            break
        meal = arg[0]
        product = arg[1]
        products = meals_types[meal][1]
        counter_meals = meals_types[meal][0]
        if len(products) == counter_meals:
            continue
        if meal in meals_types and product not in meals_types[meal][1]:
            products.append(product)

    result = []
    if len(meals_types[meal1][1]) == 0 and len(meals_types[meal2][1]) == 0 and len(meals_types[meal3][1]) == 0:
        return "No products in the cart!"

    for meal, values in sorted(meals_types.items(), key=lambda x: (-len(x[1][1]), x[0])):
        result.append(f'{meal}:')
        if len(values[1]) > 0:
            for product in sorted(values[1]):
                result.append(f' - {product}')

    return '\n'.join(result)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
