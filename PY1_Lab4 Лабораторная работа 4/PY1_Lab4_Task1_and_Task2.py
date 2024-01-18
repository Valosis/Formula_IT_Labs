# PY1_Lab4_Task1_JSON_read_multiply_and_sum.py

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


# =========================================

# Файл для задания 2 не загрузился почему-то отдельно, поэтому добавлю как часть этого

# PY1_Lab4_Task2_CSV_to_JSON_convert.py

# TODO импортировать необходимые молули
import json, csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:

    list_of_dicts = []

    with open(INPUT_FILENAME, 'r') as file:
        reader = csv.DictReader(file, delimiter = ',', lineterminator = "\r\n")
        # Чтение данных
        for row in reader:
            list_of_dicts.append(row)

        #print(list_of_dicts)

    # Запись данных в файл в формате JSON
    indent = 4  
    ensure_ascii = True  
    with open(OUTPUT_FILENAME, 'w') as file:
        json.dump(list_of_dicts, file, indent=indent, ensure_ascii=ensure_ascii)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
