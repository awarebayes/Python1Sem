# Лабораторная работа No10
# Задан текст массивом строк. Текст — фрагмент литературного произведения (5-7 предложений). Ни одна строка не оканчивается точкой кроме последней.
# Текст задается в программе, пользовательский ввод не требуется.
# Необходимо создать меню, выполняющее следующие действия:
# 1. Выравнивание текста по левому краю.
# 2. Выравнивание текста по правому краю.
# 3. Выравнивание текста по ширине.
# 4. Удаление заданного слова.
# 5. Замена одного слова другим во всем тексте.
# 6. Вычисление арифметического выражения.
# 7. Найти наиболее часто встречающееся слово в каждом предложении.
# Написал Щербина МА ИУ7-15

from expr_tree import eval_string
from collections import Counter

"""
text = [
    "Лорем ипсум долор сит    2+3-4*(4)   амет, ут вим 3 - 6  елитр иисяуе сцрибентур. При не яуалисяуе аргументум",
    "Ерат мунди пертинах но еам, ат про дицант поссит адверсариум Денияуе яуалисяуе те вис, солет апериам но яуи",
    "Оптион волуптатибус ут при еум ех лабитур цонсулату сплендиде, одио ессент те пер",
    "При ин фуиссет f f f f f f f f f аццусам трацтатос, не аугуе детерруиссет нец Не алияуид репудиандае еам,",
    "Еи аеяуе фацилис вел санцтус медиоцритатем дуо (8 + 2) * ( ( ( 82 * 3    ) - √(6%3))) те, но дицунт диссентиунт сед не вим фацер",
    "Иуварет маиорум, цум ин репримияуе неглегентур, те елит граеце витуперата вел Но нец иллуд путант, цу пауло еуисмод вел.",
]
"""

text = ["i", ]



# align right
def print_align_right():
    max_len = max(map(len, text))
    for sentence in text:
        spaces_to_add = max_len - len(sentence)
        print(" " * spaces_to_add, end="")
        print(sentence)

# align left
def print_align_left():
    max_len = max(map(len, text))
    for sentence in text:
        spaces_to_add = max_len - len(sentence)
        print(sentence, end="")
        print(" " * spaces_to_add)

# align with
def print_align_width():
    max_len = max(map(len, text))
    for sentence in text:
        sentence = " ".join(sentence.split())  # delete excess spaces
        spaces_to_add = max_len - len(sentence)  # number of space to add
        splitted = sentence.split()
        n_characters = sum(map(len, splitted))  # number of characters
        n_words = len(splitted)  # number of words
        if len(splitted) == 0:
            print(sentence)
            return
        mean_space = spaces_to_add // len(splitted) + 1  # mean len of space
        remaining_space_len = (
            max_len - n_characters - mean_space * (n_words - 1)
        )  # remaining number of spaces to spare
        remaining_space_len = max(remaining_space_len, 0)

        for word in splitted:
            print(word, end="")
            print(" " * mean_space, end="")
            if remaining_space_len > 0:
                print(" ", end="")
                remaining_space_len -= 1
        print()

# delete word
def delete_word(to_replace):
    for idx, sentence in enumerate(text):
        text[idx] = " ".join([word for word in sentence.split(" ") if word != to_replace])


# replace word
def replace_word(to_replace, replace_with):
    for idx, sentence in enumerate(text):
        text[idx] = " ".join(
            [word if word != to_replace else replace_with for word in sentence.split(" ")]
        )


# find math expression in text
def scan_for_expressions(string):
    expr = [""]
    for i in string:
        if i.isdigit() or i in "+-/*%^√()": # math symbol
            expr[-1] += i
        elif i == " " and expr[-1] != "": # space
            expr[-1] += i
        else: # no need for multiple ""
            if expr[-1] != "":
                expr.append("")

    # filter out junk
    expr = filter(lambda e: e != " " and e != "", expr)
    return expr


# evaluate all expressions in string 
def eval_all_in_string(string):
    expressions = scan_for_expressions(string)
    for expr_str in expressions:
        try:
            # evaluate
            evaluated = str(eval_string(expr_str))
        except:
            continue
        # add result
        # print(expr_str, "=", evaluated)
        string = string.replace(expr_str, evaluated + " ")
    return string

# evaluate the entire text
def eval_text():
    for idx, sentence in enumerate(text):
        text[idx] = eval_all_in_string(sentence)

# find word with max frequency
def find_max_freq():
    for idx, sentence in enumerate(text):
        counted = Counter(sentence.split())
        most_common = counted.most_common(1)[0]
        print(f"Sentence: {idx+1}, most common word:", most_common[0], f"({most_common[1]})")


def main():
    while True:
        print(
            """
        # 1. Выравнивание текста по левому краю.
        # 2. Выравнивание текста по правому краю.
        # 3. Выравнивание текста по ширине.
        # 4. Удаление заданного слова.
        # 5. Замена одного слова другим во всем тексте.
        # 6. Вычисление арифметического выражения.
        # 7. Индивидуальное задание.
        """
        )
        option = int(input(">>> option: "))
        if option == 1:
            print_align_left()
        elif option == 2:
            print_align_right()
        elif option == 3:
            print_align_width()
        elif option == 4:
            delete_word(input(">>> word to delete: "))
        elif option == 5:
            to_replace = input(">>>to_replace: ")
            replace_with = input(">>> replace_with: ")
            replace_word(to_replace, replace_with)
        elif option == 6:
            eval_text()
        elif option == 7:
            find_max_freq()


if __name__ == "__main__":
    main()
