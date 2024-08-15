
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

creating_and_writing_a_file(['1.txt', '2.txt', '3.txt'])
