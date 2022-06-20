def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    basket = {}
    for product, values in kwargs.items():
        price, quantity = values
        total_price = price * quantity
        if total_price <= budget:
            basket[product] = total_price
            budget -= total_price
        if len(basket) == 5:
            break

    result = []
    for product, total_price in basket.items():
        result.append(f"You bought {product} for {total_price:.2f} leva.")
    return '\n'.join(result)


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
