import os
def add_files(folder_path='sorted'):
    files_data = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                files_data.append((filename, text.count('\n') + 1, text))
    files_data.sort(key=lambda item: item[1])
    common_file = 'add_files.txt'
    with open(common_file, 'w', encoding='utf-8') as f_com:
        for filename, n_lines, lines in files_data:
            f_com.write(filename + '\n' + str(n_lines) +'\n')
            f_com.writelines(lines)
            f_com.write('\n')

    print(f_com)
