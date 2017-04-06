# User Agents.

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
os_count = {'Windows': 0, 'Ubuntu': 0, 'Unknown': 0, 'OS X': 0}
for line in f:
    flag_os = 0
    user_agent = my_split(line)[8]
    if 'Windows' in user_agent:
        flag_os = 1
        os_count['Windows'] += 1
    if 'Ubuntu' in user_agent:
        flag_os = 1
        os_count['Ubuntu'] += 1
    if 'Macintosh' in user_agent:
        flag_os = 1
        os_count['OS X'] += 1
    if flag_os == 0:
        os_count['Unknown'] += 1
f.close()

for k, v in sorted(os_count.items(), key=lambda x: x[1]):
    print(k, ': ', v, sep='')
