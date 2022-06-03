# def age_assignment(*args, **kwargs):
#     people_info = {}
#     for name in sorted(args):
#         first_letter = name[0]
#         for key, value in kwargs.items():
#             if key == first_letter:
#                 people_info[name] = value
#
#     result = [f"{name} is {age} years old." for name,age in people_info.items()]
#     return '\n'.join(result)


def age_assignment(*args, **kwargs):
    people_info = {}
    for name in sorted(args):
        first_letter = name[0]
        age = kwargs[first_letter]
        people_info[name] = age

    result = [f"{name} is {age} years old." for name, age in people_info.items()]
    return '\n'.join(result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
