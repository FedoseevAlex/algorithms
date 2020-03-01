from collections import Counter


class Node:
    """
    Класс ноды бинарного дерева.
    """

    def __init__(self):
        """
        В конструкторе создаются два поля класса для левого и правого
        ребенка соответственно.
        """
        self.left = None
        self.right = None

    @property
    def weight(self):
        """
        Свойство расчета веса данной вершины.
        Для каждого ребенка проверяется его тип, в зависимости от
        типа вычисляется вес ребенка. Результирующий вес ноды равен
        сумме весов детей.
        """
        if isinstance(self.left, tuple):
            left_weight = self.left[1]
        else:
            left_weight = self.left.weight() if self.left is not None else 0

        if isinstance(self.right, tuple):
            right_weight = self.right[1]
        else:
            right_weight = self.right.weight() if self.right is not None else 0

        return left_weight + right_weight


def build_tree(input_string: str) -> Node:
    """
    Функция построения дерева частот для дальнейшего создания кода Хаффмана.

    :param input_string: Входная строка для которой строится дерево
    :return: Корень дерева частот
    """
    counter = sorted(Counter(input_string).items(),
                     key=lambda x: x[1])

    # В цикле происходит жадный шаг алгоритма.
    # На каждой итерации в дерево будут объединены символы
    # c наименьшей частотой. Шаги будем продолжать до тех пор
    # пока в массиве не останется только корень дерева.
    while True:
        root = Node()
        root.left = counter.pop(0)
        root.right = counter.pop(0) if counter else None
        counter.append((root, root.weight))
        if len(counter) == 1:
            break
        counter.sort(key=lambda x: x[1])
    return counter[0]


def make_code(struct, prefix: str = "") -> list:
    """
    Функция, создающая код Хаффмана для переданного дерева
    частот символов.
    Эта функция рекурсивно обойдет переданное дерево в
    глубину и вернет список пар: (символ, код символа)

    :param struct: Дерево частот символов строки
    :param prefix: Параметр, накапливающий код символа
    :return: Список пар
    """
    answer = []
    tree, _ = struct

    if isinstance(tree, str):
        answer.append((tree, prefix))
    elif isinstance(tree, Node):
        if tree.left is not None:
            answer.extend(make_code(tree.left, prefix + "0"))
        if tree.right is not None:
            answer.extend(make_code(tree.right, prefix + "1"))
    return answer


def prepare_answer(input_string: str) -> str:
    """
    Функция подготовки ответа для тестов

    :param input_string: Строка для которой будет построен код
    Хаффмана
    :return: Строка с ответом на задание
    """
    answer = list()
    tree = build_tree(input_string)
    codes = dict(make_code(tree))
    letters_num = len(codes)
    coded_sequence = [codes[letter] for letter in input_string]
    coded_string = "".join(coded_sequence)
    answer.append(f"{letters_num} {len(coded_string)}")
    answer.append(coded_string)
    for letter, code in codes.items():
        answer.append(f"{letter}: {code}")

    return "\n".join(answer)


if __name__ == "__main__":
    inp = input()
    print(prepare_answer(inp))
