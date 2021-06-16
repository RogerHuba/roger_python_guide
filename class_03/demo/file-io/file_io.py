spam = open('assets/spam.txt', 'r')

print(spam)

content = spam.read()

print(content)

# for word in content:
#     print(word)

# for word in content.split(' '):
#     print(word)

print('Is file closed?', spam.closed)
spam.close()
print('Is file closed?', spam.closed)

help(spam)

print(dir(spam))

help(open)

with open('assets/brain.jpg', 'rb') as f:
    contents = f.read()

# [ Initial : End : IndexJump ]

for x in contents[:128]:
    print(type(contents))

with open('assets/brain.copy.jpg', 'wb') as f2:
    f2.write(contents)