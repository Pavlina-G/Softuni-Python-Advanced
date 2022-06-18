def start_spring(**kwargs):

    spring_objects = {}
    for key, value in sorted(kwargs.items()):
        if value not in spring_objects:
            spring_objects[value] = []
        spring_objects[value].append(key)

    sorted_object = dict(sorted(spring_objects.items(), key=lambda x: (-len(x[1]), x[0])))
    result = []
    for type, values in sorted_object.items():
        result.append(f"{type}:")
        for value in values:
            result.append(f"-{value}")
    return '\n'.join(result)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}

print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))


