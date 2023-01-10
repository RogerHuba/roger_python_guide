def square_tuple1(tpl):
    squares = []
    for num in tpl:
        squares.append(num * num)
    return squares


def square_tuple2(tpl):
    squares = [num ** 2 for num in tpl]
    return squares


if __name__ == "__main__":
    sq_return1 = square_tuple1((1, 2, 3, 4, 5))
    assert sq_return1 == [1,4,9,16,25]
    sq_return2 = square_tuple2((1, 2, 3, 4, 5))
    assert sq_return2 == [1,4,9,16,25]

