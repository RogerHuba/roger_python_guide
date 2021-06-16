from data_structures.tree.tree import Node


def balanced_binary_tree(root: Node) -> bool:
    is_balanced = True

    def traverse(node: Node) -> int:
        if not node:
            return 0

        L = traverse(node.left)
        R = traverse(node.right)

        nonlocal is_balanced
        if abs(L - R) > 1:
            is_balanced = False

        return 1 + max(L, R)

    traverse(root)

    return is_balanced
