from collections import Counter
from operator import itemgetter
from pprint import pprint


def prepare_answer_encode() -> str:
    """
    Функция подготовки ответа для тестов на создание кода Хаффмана.

    :return: Строка с ответом на задание
    """
    input_string = input()
    answer = list()
    code = make_code(input_string)
    translation_table = str.maketrans(code)
    encoded_string = input_string.translate(translation_table)
    answer.append(f'{len(code.keys())} {len(encoded_string)}')
    for letter, coding in code.items():
        answer.append(f'{letter}: {coding}')
    answer.append(encoded_string)
    return "\n".join(answer)


def make_code(input_string: str) -> dict:
    """
    Построение дерева по заданной строке

    :param input_string: Строка для которой будет построено дерево
    частот
    :return: Список из символа, его частоты и списка для кода Хаффмана
    """
    counts = list(Counter(input_string).items())
    codes = {key[0]: '' for key in counts}

    while True:
        counts.sort(key=itemgetter(1))

        left_letter, left_weight = counts.pop(0)
        for letter in left_letter:
            codes[letter] = '0' + codes[letter]

        right_letter, right_weight = counts.pop(0) if counts else ('', 0)
        for letter in right_letter:
            codes[letter] = '1' + codes[letter]
        counts.append((left_letter + right_letter, left_weight + right_weight))

        if len(counts) == 1:
            break
    return codes


def prepare_answer_decode():
    """
    Функция для разбора строк с кодом Хаффмана для символов
    и вывода результата для тестов.
    """
    symbols_num, _ = input().split()
    symbols_num = int(symbols_num)

    codes = dict()
    for _ in range(symbols_num):
        symbol, code = input().split(': ')
        codes[code] = symbol
    encoded_string = input()

    current = ''
    result = ''
    for symbol in encoded_string:
        current += symbol
        if current not in codes:
            continue
        result += codes[current]
        current = ''
    return result


if __name__ == "__main__":
    print(prepare_answer_decode())
