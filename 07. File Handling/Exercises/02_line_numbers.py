import re


def adding_line_nums(file_path):
    with open(file_path,'r') as file:
        result = dict()
        for i, line in enumerate(file):
            result[f'Line {i+1}:'] = line.strip()
        return result


def count_words_and_symbols(dict_lines):
    letter_pattern = r'[a-zA-Z]'
    symbol_pattern = r'[^a-zA-Z0-9 ]'
    output_dict = {}
    for key, line in dict_lines.items():
        letter_count = len(re.findall(letter_pattern, line))
        symbol_count = len(re.findall(symbol_pattern, line))
        output_dict[key]= {}
        output_dict[key][line] = f'({letter_count})({symbol_count})'
    return output_dict


def create_output_file(result, file_path):
    with open(file_path, 'w') as file:
        for key, nested_dict in result.items():
            for line, nums in nested_dict.items():
                file.writelines(f'{key} {line} {nums}\n')


lines_num = adding_line_nums('02_text.txt')
result_dict = count_words_and_symbols(lines_num)
output_file = create_output_file(result_dict, './output.txt')
