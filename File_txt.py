
import os

def creating_and_writing_a_file(list_of_files):
    sort_files = sorted_txt_file(list_of_files)
    # print(sort_files)
    my_file = open("result_txt.txt", "w+")
    for txt in sort_files:
        print(txt)
        my_file.writelines(txt)
    my_file.close()

def sorted_txt_file(list_of_files):
    resalt = []
    for name_file in list_of_files:
        txt_list = []
        with open(name_file, 'r', encoding='utf-8') as file:
            for line in file:
                txt_list.append((line.strip()) + '\n')
            txt_list.insert(0, (str(len(txt_list)) + '\n'))
            txt_list.insert(0, name_file + '\n')
            resalt.append(txt_list)      
    resalt.sort(key=len)
    return resalt 

#creating_and_writing_a_file(['1.txt', '2.txt', '3.txt'])

def merge_files(file_names):
    sorted_file_data = sorted(((name, len(open(name, encoding='utf-8').readlines())) for name in file_names), key=lambda x: x[1])
    with open('result2.txt', 'w', encoding='utf-8') as result_file:
        for file_name, line_count in sorted_file_data:
            file_content = open(file_name, encoding='utf-8').read()
            result_file.write(f'Имя файла: {file_name}\n')
            result_file.write(f'Количество строк: {line_count}\n')
            result_file.write(file_content.strip() + '\n\n')

merge_files(['1.txt', '2.txt', '3.txt'])


