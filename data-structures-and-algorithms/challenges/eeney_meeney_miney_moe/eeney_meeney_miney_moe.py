from data_structures.linked_list.linked_list import LinkedList


def circle_ll(ll: LinkedList) -> LinkedList:
    """Create a circular LL from a given singly linked LL

    Args:
        ll (LinkedList): LL to be modified

    Returns:
        LinkedList: Modified LL
    """
    curr = ll.head
    while curr.next:
        curr = curr.next
    curr.next = ll.head

    return ll


def eeney_meeney_miney_moe(names: list, k: int) -> str:
    """Play the Eeney Meeney Miney Moe game with a given list of names and an integer k that defines what person should be removed from the list. The game continues before only 1 person is left

    Args:
        names (list): Names of the people playing the game
        k (int): On what count the person should leave the game

    Returns:
        str: Name of the winnig person
    """

    # Create a LL with indexes matching the given names length
    ll = LinkedList()
    for i in range(len(names)):
        ll.append(i)

    ll = circle_ll(ll)

    # Get the last left index
    curr = prev = ll.head
    count = 0
    while curr.next != curr:
        count += 1
        if not count % k:
            prev.next = curr.next
        prev, curr = curr, curr.next
    idx = curr.val

    return names[idx]


def eeney_meeney_miney_moe_math(names, k):
    # CREDITS: https://www.reddit.com/r/theydidthemath/comments/3oklvn/request_what_is_the_equation_for_eeny_meeny_miny/
    L = len(names)

    if L > k:
        return names[k]
    elif L > k / 2:
        return names[2 * L - k]
    else:
        return names[(k - L)/(L - 1)]
