def get_info(name, age, town):
    return f"This is {name} from {town} and he is {age} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))

info1 = {
    'name': 'Pesho',
    'town': 'Burgas',
    'age': 18,
}

info2 = {
    'name': 'Gosho',
    'town': 'Stara Zagora',
    'age': 48,
}

print(get_info(**info1))
print(get_info(**info2))