"""
This module contains solution for stepik task
https://stepik.org/lesson/13238/step/10?auth=login&unit=3424
"""


def pack(capacity, items):
    """
    This function packs items to make payload maximum valuable
    Returns value of rucksack payload
    """
    # Filter items with 0 cost
    items = filter(lambda item: item[0] != 0, items)
    items = sorted(items, key=lambda item: item[1] / item[0], reverse=False)
    cost = 0
    for value, amount in items:
        if capacity == 0:
            break

        if amount > capacity:
            cost += value * capacity / amount
            break
        else:
            cost += value
            capacity -= amount

    return cost


if __name__ == "__main__":
    item_num, capacity = map(int, input().strip().split())
    items = list()
    for _ in range(item_num):
        items.append(tuple(map(int, input().strip().split())))

    result = pack(capacity, items)
    print(f"{result:.3f}")
