# TODO решите задачу
import json


def task() -> float:
    filename = 'input.json'
    # Чтение данных из файла в формате JSON
    with open(filename) as file:
        data = json.load(file)

    sum_ = 0
    for elem in data:
        sum_ += elem["score"] * elem["weight"]

    precision = 3
    return round(sum_, precision)


print(task())
