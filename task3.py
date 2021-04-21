def joining_files(path_to_catalogue):
    import os
    list_of_files = os.listdir(path_to_catalogue)
    lines = []
    for file in list_of_files:
        with open(os.path.join(path_to_catalogue, file), "r", encoding = 'utf-8') as f:
            temp_list = f.readlines()
            lines.append((file, len(temp_list), temp_list))
    a = sorted(lines, key=lambda text: text[1])
    result = open("result.txt", "w", encoding='utf-8')
    for line in a:
        result.write(line[0])
        result.write('\n')
        result.write(str(line[1]))
        result.write('\n')
        for line in line[2]:
            result.write(line)
        result.write('\n')
    result.close()
    return

path = r'C:\Users\kuzne\Desktop\Python\pythonProject1\t3'
print (joining_files(path))



