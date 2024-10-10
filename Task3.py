import os
def add_files():
    path_1 = '1.txt'
    path_2 = '2.txt'
    path_3 = '3.txt'
    file_1 = os.path.join(os.getcwd(), path_1)
    file_2 = os.path.join(os.getcwd(), path_2)
    file_3 = os.path.join(os.getcwd(), path_3)
    common_file = 'add_files.txt'
    with open(file_1, 'r', encoding='utf-8') as f_1:
        f_1_added = f_1.readlines()
    with open(file_2, 'r', encoding='utf-8') as f_2:
        f_2_added = f_2.readlines()
    with open(file_3, 'r', encoding='utf-8') as f_3:
        f_3_added = f_3.readlines()
    with open(common_file, 'w', encoding='utf-8') as f_com:
        if min(len(f_1_added)) and len(f_2_added) < len(f_3_added):
            f_com.write(path_1, path_2, path_3)
        elif min(len(f_2_added)) and len(f_1_added) < len(f_3_added):
            f_com.write(path_2, path_1, path_3)
        elif min(len(f_3_added)) and len(f_2_added) < len(f_1_added):
            f_com.write(path_3, path_2, path_1)
        elif min(len(f_1_added)) and len(f_3_added) < len(f_2_added):
            f_com.write(path_1, path_3, path_2)
        elif min(len(f_2_added)) and len(f_2_added) < len(f_1_added):
            f_com.write(path_2, path_3, path_1)
        else:
            f_com.write(path_3, path_1, path_2)

        lines = f_com.readlines()

        print(f_com.name)
        print(len(lines))
        print(f_com)
