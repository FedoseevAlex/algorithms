"""
https://m.habr.com/ru/company/yandex/blog/488682/

Удаление пустых значений

Напишите программу, которая из JSON-структуры удаляет значения, являющиеся пустыми словарями ({})
или пустыми списками ([]), до тех пор, пока есть такие значения.
Если удаляется значение в словаре, то удаляется и соответствующий ключ.
Ограничение времени: 0,2 с, ограничение памяти: 6 МБ.

Формат ввода
В единственной строке входных данных содержится строка длины n (1 ≤ n ≤ 1000).
 Гарантируется, что эта строка является правильной JSON-строкой.

Формат вывода:
Выведите через пробел количество удаленных пустых словарей и количество удаленных пустых списков.
"""

import json

from pprint import pprint


SAMPLE_DATA = """
{
   "colors":[
      {
         "color":"black",
         "category":"hue",
         "type":"primary",
         "code":{
            "rgba":[
               [

]
],
            "hex":"#000"
}
},
      {
         "color":"white",
         "category":"value",
         "code":{
            "rgba":[
               0,
               0,
               0,
               1
],
            "hex":"#FFF"
}
},
      {
         "color":"red",
         "category":"hue",
         "type":"primary",
         "code":{
            "rgba":[
               255,
               0,
               0,
               1
],
            "hex":"#FF0"
}
},
      {
         "color":"blue",
         "category":"hue",
         "type":"primary",
         "code":{
            "rgba":[
               0,
               0,
               255,
               1
],
            "hex":"#00F"
}
},
      {
         "color":"yellow",
         "category":"hue",
         "type":"primary",
         "code":{
            "rgba":[
               255,
               255,
               0,
               1
],
            "hex":"#FF0"
}
},
      {

},
      {
         "color":"green",
         "category":"hue",
         "type":"secondary",
         "code":{
            "rgba":[
               0,
               255,
               0,
               1
],
            "hex":"#0F0"
}
}
],
   "empty_field":[
],
   "nested_empty_field":{
      "real_empty":[
]
},
   "not_so_empty":[
      [

]
]
}
"""


def collapse(structure: dict) -> int:
    n = 0

    for key, value in structure.copy().items():
        if isinstance(value, dict):
            n += collapse(structure[key])
        if not value:
            n += 1
            structure.pop(key)
            continue
    return n


if __name__ == "__main__":
    data = json.loads(SAMPLE_DATA)
    print(collapse(data))
    pprint(data)
