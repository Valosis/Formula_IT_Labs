# TODO Напишите функцию для поиска индекса товара
def get_item_index(items, find_item):
    for i, item in enumerate(items):
        if item == find_item:
            # The find_item has been found, return its index
            return i

    # The find_item hasn't been found, return None
    return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    item_index = get_item_index(items_list, find_item)
    if item_index is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {item_index}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")