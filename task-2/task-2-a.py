# Ответы сервера.

def my_split(string):
    result = []
    word = []
    """flag = 0 --- out of [] and "";
    1 --- inside [; 2 --- inside "

    """
    flag = 0
    for char in string:
        if flag == 0:
            if char == '[':
                flag = 1
            elif char == '"':
                flag = 2
            elif char == ' ':
                if word:
                    result.append(''.join(word))
                    word.clear()
            else:
                word.append(char)
        elif flag == 1 and char == ']' or \
                flag == 2 and char == '"':
            result.append(''.join(word))
            word.clear()
            flag = 0
        else:
            word.append(char)
    if word:
        result.append(''.join(word))
    return result

f = open('input.txt', 'r')
task_a = 0
task_b = 0
task_c = 0
task_d = 0

for line in f:
    task_d += 1
    analyze = my_split(line)
    code = int(analyze[5])
    if code == 200:
        task_a += 1
    elif 300 <= code <= 309:
        task_b += 1
    else:
        task_c += 1
f.close()

print(task_a)
print(task_b)
print(task_c)
print(task_d)
