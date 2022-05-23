def chars_dict(text):
    chars = dict()
    for ch in text:
        if ch not in chars:
            chars[ch] = 1
        else:
            chars[ch] += 1

    return chars


text = tuple(sorted(input()))
letters = chars_dict(text)

for char, value in letters.items():
    print(f"{char}: {value} time/s")
