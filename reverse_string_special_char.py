''''
Reverse words in a given sentence with special characters in place
Example: Hello! How’re you?
Output: olleH! woH’er uoy?


a-z 97 to 122
A-Z 65 to 90
0-9 48 to 57
'''

#special_chars = ['\'', '"', ',', '?', '!', '@', '#', '$', '%', '^', '&', '*', '(', ")"]


def is_special_char(c):
    if (ord(c) >= 97 and ord(c) <=122)  or \
            (ord(c) >= 65 and ord(c) <= 90 ) or \
            (ord(c) >=48 and ord(c) <=57):
        return False
    return True


def reverse_str(input_string):
    special_char_index = []
    for i in range(len(input_string)):
        if is_special_char(str(input_string[i])):
            special_char_index.append(i)

    if len(special_char_index) > 0:
        final_str = ''
        current_index = 0
        # adding substring except lastone
        for index in special_char_index:
            end_index = index
            final_str = final_str + input_string[current_index:end_index][::-1]
            final_str = final_str + input_string[index]
            current_index = index + 1

        # adding last subString
        final_str = final_str + input_string[current_index:len(input_string)][::-1]
        return final_str
    else:
        return input_string[::-1]


def reverse_special_chars(input_string):
    input_string_list = input_string.split(' ')
    op_string_list = []
    op_str = ''
    for item in input_string_list:
        #op_string_list.append(reverse_str(item))
        op_str = op_str + reverse_str(item) + ' '
    return op_str.strip()



if __name__ == "__main__":
    #print(is_special_char('a'))
    #reverse_str('rah!ul!abc')
    print(reverse_special_chars('Hello! How’re you?'))
