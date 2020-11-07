# Написать программу, которая позволит с использованием меню:
# 1. Проинициализировать список первыми N элементами заданного ряда
# 2. Добавить элемент в произвольное место списка
# 3. Удалить произвольный элемент из списка
# 4. Очистить список
# 5. Найти значение K-го экстремума в списке, если он является списком чисел
# 6. Найти наиболее длинную последовательность чисел по варианту
# 7. Найти последовательность, включающую в себя наибольшее количество
#  элементов-строк по варианту
#  Написал: Щербина МА ИУ7  15Б

from random import randint

seq = []
seq_type = "float"
VOWELS = ("a", "e", "i", "o", "u", "а", "у", "е", "ы", "о", "э", "я", "и", "ю", "ё")


while True:
    print(
        """
    1. Проинициализировать список первыми N элементами заданного ряда
    2. Добавить элемент в произвольное место списка
    3. Удалить произвольный элемент из списка
    4. Очистить список
    5. Найти значение K-го экстремума в списке, если он является списком чисел
    6. Найти наиболее длинную последовательность чисел по варианту
    7. Найти последовательность, включающую в себя наибольшее количество
       элементов-строк по варианту 
    8. Ввести список
    9. Вывести список
    """
    )

    choice = int(input(">>> your choice (int+): "))
    if choice == 1:
        x = float(input(">>> x (float): "))
        n_elems = int(input(">>> n_elements == len(list), (int+): "))
        seq = [0] * n_elems  # sequence represented as list
        seq_type = "float"

        x_n = x  # first term
        i = 3  # factorial iterator
        step = 0  # while loop iterator
        while True:
            # calculate n th term
            x_n *= -1 * x * x / i
            i += 2

            # check if still in boundaries
            if step >= n_elems:
                break

            # update loop variable and sum
            seq[step] = x_n
            step += 1

        print(f"1. Initialized a list of first {n_elems}, sequence is arctan(x):")
        print("__________________")
        for idx, i in enumerate(seq):
            print(f"{idx:<4}", f"{i:g}")
        print("__________________")

    if choice == 2:
        x_n = int(input(">>> value of element (any)"))
        x_n_place = int(input(">>> index of element to add at (int)"))
        if x_n_place >= len(seq):
            print("index is too large!")
            continue
        print(f"2. Adding a new element {x_n:g} at {x_n_place}")
        seq.insert(x_n_place, x_n)
        print(f"2. Now seq[{x_n_place}] is {seq[x_n_place]:g}")

    if choice == 3:
        x_n_place = int(input(">>> index of element to delete at (int)"))
        print(f"3. Deleting {x_n_place}'th element from seq")
        seq.pop(x_n_place)
        print(f"3. now seq[{x_n_place}] is {seq[x_n_place]:g}")

    if choice == 4:
        print("4. Clearing the list")
        seq.clear()
        print(f"4. Now seq is {seq}")

    if choice == 5:

        if seq_type != "float":
            print("Not supported for", seq_type, "float only")
            continue

        k = int(input(">>> number k of k'th extremum in list (int+): "))
        assert k > 0
        if len(seq) < 2:
            print("Can't find an extremum in a list, len<2")

        n_extremum = 0
        for i in range(1, len(seq) - 1):
            if seq[i - 1] > seq[i] < seq[i + 1]:  # minima
                n_extremum += 1
            elif seq[i - 1] < seq[i] > seq[i + 1]:  # maxima
                n_extremum += 1
            if n_extremum == k:  # we've found it
                print(f"{k}'th extremum is {seq[i]}")
                break
            if i == len(seq) - 2:  # search length exceeded
                print(f"No {k}'th extremum found")

    # Убывающая последовательность отрицательных чисел, модуль которых является простым числом:
    if choice == 6:

        if seq_type != "float":
            print("Not supported for", seq_type, "float only")
            continue

        max_start, start = 0, 0
        max_end, end = 0, 0
        for idx, i in enumerate(seq):
            is_prime = False
            # check if prime
            if float(i).is_integer():  # check if integer first
                if i in [0, 1]:
                    is_prime = True
                for divisor in range(2, abs(num)):
                    if i % divisor == 0:
                        is_prime = True
                        break

            if is_prime:
                end = idx
            else:
                start = idx + 1
                end = idx + 1

            if end - start > max_end - max_start:
                max_end = end
                max_start = start

        print(
            "Убывающая последовательность отрицательных чисел, модуль которых является простым числом:"
        )
        print("Max sequence starts at", max_start)
        print("Max sequence ends at", max_end)
        print("__________________")
        for idx, i in enumerate(seq[max_start : max_end + 1]):
            print(f"{idx+max_start:<4}", f"{i}")
        print("__________________")

    # 1. Строк, содержащих только гласные буквы.
    if choice == 7:
        if seq_type != "string":
            print("Not supported for", seq_type, "string only")
            continue

        max_start, start = 0, 0
        max_end, end = 0, 0
        for idx, i in enumerate(seq):
            all_vowels = True
            for char in i:
                if char.lower() not in VOWELS:
                    all_vowels = False
                    break

            if all_vowels:
                end = idx
            else:
                start = idx + 1
                end = idx + 1

            if end - start > max_end - max_start:
                max_end = end
                max_start = start

        print("Строк, содержащих только гласные буквы.")
        print("Max sequence starts at", max_start)
        print("Max sequence ends at", max_end)
        print("__________________")
        for idx, i in enumerate(seq[max_start : max_end + 1]):
            print(f"{idx+max_start:<4}", f"{i}")
        print("__________________")

    if choice == 8:
        print("Sir, I shall enquire thou to input a list thee desireth")
        n = int(input(">>> n_elems in your list (int+): "))
        seq_type = input(">>> type of your sequence [float, string]: ")
        if seq_type not in ["float", "string"]:
            print("Bad seq type!")
            continue
        seq = [0] * n

        # read seq
        for i in range(n):
            seq[i] = input(f">>> seq[{i}]= ")
            if seq_type == "float":
                seq[i] = float(seq[i])

    if choice == 9:
        print("Type is", seq_type)
        print("__________________")
        for idx, i in enumerate(seq):
            print(f"{idx:<4}", f"{i}")
        print("__________________")

    if choice > 9:
        print("bad choice!")
