max_value = 1000


def outer_scope():
    global max_value
    max_value = 1000
    print(f'This is the outer max: {max_value}')

    def inner_scope():
        nonlocal max_value

        max_value = 99999
        print(max_value)

    inner_scope()


if __name__ == '__main__':
    outer_scope()
