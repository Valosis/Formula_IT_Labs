# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group_str, participants_second_group_str, participants_delimiter = ","):
    participants_first_group_list = participants_first_group_str.split(participants_delimiter)
    participants_second_group_list = participants_second_group_str.split(participants_delimiter)
    
    intersection_set = set(participants_first_group_list).intersection(participants_second_group_list)
    return sorted(list(intersection_set))
  
# TODO Проверьте работу функции с разделителем отличным от запятой
def main_func():
    participants_first_group_str = "Иванов|Петров|Сидоров"
    participants_second_group_str = "Петров|Сидоров|Смирнов"
    participants_delimiter = "|"

    return find_common_participants(participants_first_group_str, participants_second_group_str, participants_delimiter)

print(main_func())