from os import walk

file_path = './'
files_dict = {}

for _,_, files in walk(file_path):
    for file in files:
        extention = f".{file.split('.')[-1]}"
        if extention not in files_dict:
            files_dict[extention] = []
        files_dict[extention].append(file)

with open(file_path + 'file_report.txt', 'w') as report_file:
    if len(files_dict) > 0:
        for key, values in sorted(files_dict.items(), key=lambda kv: (kv[0], kv[1])):
            report_file.write(f"{key}\n")
            for value in values:
                report_file.write(f"- - - {value}\n")
report_file.close()


