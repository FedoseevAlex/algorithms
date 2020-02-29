from collections import Counter
import heapq


class Node:
    def __init__(self):
        self.left = None
        self.right = None

    @property
    def weight(self):
        if isinstance(self.left, tuple):
            left_weight = self.left[0]
        else:
            left_weight = self.left.weight() if self.left is not None else 0

        if isinstance(self.right, tuple):
            right_weight = self.right[0]
        else:
            right_weight = self.right.weight() if self.right is not None else 0

        return left_weight + right_weight

    def __lt__(self, _):
        return True

    __gt__ = __lt__


def build_tree(input_string: str):
    counter = [(weight, letter) for letter, weight in Counter(input_string).items()]
    heapq.heapify(counter)
    while len(counter) >= 2:
        root = Node()
        root.right, root.left = heapq.heappop(counter), heapq.heappop(counter)
        heapq.heappush(counter, (root.weight, root))
    return counter[0]


def make_code(struct, prefix=""):
    answer = []
    _, tree = struct

    if isinstance(tree, str):
        answer.append((tree, prefix))
    elif isinstance(tree, Node):
        answer.extend(make_code(tree.left, prefix + '0'))
        answer.extend(make_code(tree.right, prefix + '1'))

    return answer


def prepare_answer(input_string):
    answer = list()
    tree = build_tree(input_string)
    codes = dict(make_code(tree))
    letters_num = len(codes)
    coded_sequence = [codes[letter] for letter in input_string]
    coded_string = ''.join(coded_sequence)
    answer.append(f'{letters_num} {len(coded_string)}')
    answer.append(coded_string)
    for letter, code in codes.items():
        answer.append(f"{letter}: {code}")

    return '\n'.join(answer)


if __name__ == "__main__":
    inp = input()
    print(prepare_answer(inp))
