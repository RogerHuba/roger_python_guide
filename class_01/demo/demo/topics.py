from import_value import value_to_import

"""Things to cover...
* What is a module
* What is a script
* How to execute it from CLI
* print/input
* string concatenation
* formatted strings
* if __name__ == "__main__": snippet
"""

print('Star Wars is the best movie?')

input('>')

movie = input('>')
print(movie)

print('Concat')
print('The best SW movie is ' + movie + '.')

print('older')
print('The best SW movie is {}.'.format(movie))

print('newer')
print(f'The best SW movie is {movie}.')


def print_movie(movie: str) -> str:
    return_string = f'The best SW movie is {movie}.'
    return return_string


print(print_movie('a'))


def new_greeting(name):
    return name

print(new_greeting('roger'))

# difference between script and module
# Script is directly executed
# Module is imported like a library

# create a new file to import something
# create a import_value.py

print(value_to_import)

multi_line = """
    Here is some text
    And some more text
    And alas there is more
"""

print(multi_line)

all_movies = ['menace', 'clones', 'sith', 'hope']

print(all_movies)
print(movie)
if movie in all_movies:
    print('It is there')
elif movie not in all_movies:
    print('It is not there')
