from data_structures.stacks_and_queues.stacks_and_queues import Queue
from data_structures.tree.k_ary_tree import Node, Tree


def fizz_buzz(val: int) -> str:
    """Return FizzBuzz if the given number is divisible by 3 and 5, Fizz if the given number is divisible by 5 and string with the given value if none of the above is true

    Args:
        val (int): Value to be processed

    Returns:
        str: Fizz, Buzz, FizzBuzz or the stringified value depending on the given value
    """
    output = None
    if not val % 15:
        output = 'FizzBuzz'
    elif not val % 3:
        output = 'Fizz'
    elif not val % 5:
        output = 'Buzz'
    else:
        output = str(val)

    return output


def fizz_buzz_tree(tree: object) -> object:
    """Traverse the given k-ary tree and replace its values in FizzBuzz manner

    Args:
        tree (object): k-ary tree

    Returns:
        object: new k-ary tree 
    """
    output = Tree()

    if tree.root:
        q1 = q2 = Queue()

        q1.enqueue(tree.root)
        output.root = Node(fizz_buzz(tree.root.val))
        q2.enqueue(output.root)

        while not q1.is_empty():
            el1, el2 = q1.dequeue(), q2.dequeue()

            for child in el1.children:
                q1.enqueue(child)
                new_el = Node(fizz_buzz(child.val))
                el2.children.append(new_el)
                q2.enqueue(new_el)

    return output
