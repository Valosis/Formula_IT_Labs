import re
RU_ALPHABET_STRING = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

# Remove all non aplhabet symbols
def remove_non_alphabet_symbols(text):
    # Using regular exressions to delete all non alphabet symbols
    # Replace everything that is not from [А-Яа-я] with '' in text
    return re.sub("[^А-Яа-я]", '', text)

# Make dictionary with letters as keys and its occurences as values 
def make_letters_count_dict(text):
    letters_count_dict = {}

    # Go through the Russian alphabet that has a CONST length and check if the letter appeared in the text.

    # P.S. Ответ на Степике имеет другой порядк букв, так как алгоритм, видимо, основан на анализе букв подряд из текста.
    # Однако данный цикл работает за O(1), а не за O(N), где N - длина текста, так как мы вынуждены проверят каждую букву.
    # К тому же про порядок букв в задании ничего не сказано
    for letter in RU_ALPHABET_STRING:
        # If YES -> add in a dictionary
        if(letter in text):
            letters_count_dict.update({letter: text.count(letter)})

    return letters_count_dict

# TODO  Напишите функцию count_letters
def count_letters(text):
    main_str_alphabet_symbols_only = remove_non_alphabet_symbols(text)
    main_str_alphabet_symbols_only = main_str_alphabet_symbols_only.lower()
    letters_count_dict = make_letters_count_dict(main_str_alphabet_symbols_only)

    return letters_count_dict



# TODO Напишите функцию calculate_frequency
def calculate_frequency(letters_count_dict, letters_number):
    letters_freq_dict = {}

    for letter in letters_count_dict:
        # P.S. указанная точность в задании - 2 цифры после запятой.
        # Но в таком случае ее не хватает для низкочастотных букв.
        precision = 2
        letters_freq_dict.update({letter: round(letters_count_dict[letter]/letters_number, precision)})

    return letters_freq_dict


def main_func():
    main_str = """
    У лукоморья дуб зелёный;
    Златая цепь на дубе том:
    И днём и ночью кот учёный
    Всё ходит по цепи кругом;
    Идёт направо — песнь заводит,
    Налево — сказку говорит.
    Там чудеса: там леший бродит,
    Русалка на ветвях сидит;
    Там на неведомых дорожках
    Следы невиданных зверей;
    Избушка там на курьих ножках
    Стоит без окон, без дверей;
    Там лес и дол видений полны;
    Там о заре прихлынут волны
    На брег песчаный и пустой,
    И тридцать витязей прекрасных
    Чредой из вод выходят ясных,
    И с ними дядька их морской;
    Там королевич мимоходом
    Пленяет грозного царя;
    Там в облаках перед народом
    Через леса, через моря
    Колдун несёт богатыря;
    В темнице там царевна тужит,
    А бурый волк ей верно служит;
    Там ступа с Бабою Ягой
    Идёт, бредёт сама собой,
    Там царь Кащей над златом чахнет;
    Там русский дух… там Русью пахнет!
    И там я был, и мёд я пил;
    У моря видел дуб зелёный;
    Под ним сидел, и кот учёный
    Свои мне сказки говорил.
    """

    letters_count_dict = count_letters(main_str)
    letters_freq_dict = calculate_frequency(letters_count_dict, sum(letters_count_dict.values()))

    # TODO Распечатайте в столбик букву и её частоту в тексте
    for letter in letters_freq_dict:
        print(letter, letters_freq_dict[letter])

main_func()