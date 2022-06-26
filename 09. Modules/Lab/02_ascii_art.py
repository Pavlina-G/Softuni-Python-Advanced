from pyfiglet import figlet_format

def print_art(text):
    # ascii_art = figlet_format(text)
    # ascii_art = figlet_format(text, font = "bubble") #  run with font
    ascii_art = figlet_format(text, font = "doh") #  run with font
    print(ascii_art)


text = input()
print_art(text)