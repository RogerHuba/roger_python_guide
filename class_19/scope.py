max_value = 999
print(f'This is the first outside max: {max_value}')

def outer_scope():
    # global max_value
    max_value = 10000
    print(f'This is the outer max: {max_value}')

    def inner_scope():
        nonlocal max_value

        max_value = 99999
        print(f'This is the inner max: {max_value}')

    inner_scope()
    print(f'This is the final outer max: {max_value}')

outer_scope()
print(f'This is the last outside max: {max_value}')

