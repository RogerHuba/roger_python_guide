# Given a string, write a function that returns a new string but only has one of each character
# Exampe: 'commissioner'
# Return: 'comisner'

my_string = 'commissioner'
tmp_list = []
final_string = ''
for char in my_string:
    if char not in tmp_list:
        tmp_list.append(char)
        final_string += char
print(final_string)

new_string = set(my_string)
print("".join(new_string))