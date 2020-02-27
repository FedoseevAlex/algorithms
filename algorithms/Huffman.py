from collections import Counter


class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def weight(self):
        left_weight = self.left.weight() if self.left is not None else 0
        right_weight = self.right.weight() if self.right is not None else 0
        return left_weight + right_weight

    def __repr__(self):
        return f"Node ({repr(self.left)} {repr(self.right)})"


class Leaf:
    def __init__(self, letter, frequency):
        self.letter = letter
        self.frequency = frequency

    def weight(self):
        return self.frequency

    def __repr__(self):
        return f"Leaf <{repr(self.letter)}, {repr(self.frequency)}>"


def build_tree(counter):
    sorted_counter = sorted(counter.items(), key=lambda kv: kv[1])
    print(sorted_counter)

    left = Leaf(*sorted_counter[0])
    root = Node(left, None)

    for index in range(1, len(sorted_counter) - 1):
        next_leaf = Leaf(*sorted_counter[index + 1])
        root.right = Leaf(*sorted_counter[index])
        if root.weight() < next_leaf.weight():
            new_root = Node(root, next_leaf)
        else:
            new_root = Node(next_leaf, root)

        root = new_root
    print(repr(root))


if __name__ == '__main__':
    inp = "abacabad"
    build_tree(Counter(inp))
