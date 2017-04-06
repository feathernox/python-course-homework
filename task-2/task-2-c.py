# Количество запросов мониторинга.

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
go_count = 0
for line in f:
    user_agent = my_split(line)[8]
    if 'Go-http-client/1.1' in user_agent:
        go_count += 1
f.close()
print(go_count)
