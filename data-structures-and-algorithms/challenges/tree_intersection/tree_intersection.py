from data_structures.stacks_and_queues.stacks_and_queues import Queue


def tree_intersection(bt1: object, bt2: object) -> set:
    output = set()
    q1 = q2 = Queue()

    if bt1.root and bt2.root:
        q1.enqueue(bt1.root)
        q2.enqueue(bt2.root)

    while not (q1.is_empty() and q2.is_empty()):
        el1, el2 = q1.dequeue(), q2.dequeue()

        if el1.val == el2.val:
            output.add(el1.val)

        if el1.left and el2.left:
            q1.enqueue(el1.left)
            q2.enqueue(el2.left)

        if el1.right and el2.right:
            q1.enqueue(el1.right)
            q2.enqueue(el2.right)

    return output
