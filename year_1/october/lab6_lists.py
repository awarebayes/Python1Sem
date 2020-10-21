# Написать программу, которая позволит с использованием меню:
# 1. Проинициализировать список первыми N элементами заданного ряда
# 2. Добавить элемент в произвольное место списка
# 3. Удалить произвольный элемент из списка
# 4. Очистить список
# 5. Найти значение K-го экстремума в списке, если он является списком чисел
# 6. Найти наиболее длинную последовательность чисел по варианту
# 7. Найти последовательность, включающую в себя наибольшее количество
# элементов-строк по варианту
#  Написал: Щербина МА ИУ7  15Б

from random import randint

seq = []


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
    """)

    choice = int(input(">>> your choice (int+): "))
    if choice == 1:
        x = float(input(">>> x (float): "))
        n_elems = int(input(">>> n_elements == len(list), (int+): ")) 
        seq = [0]*n_elems # sequence represented as list

        x_n =  x # first term
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
        x_n_place = randint(0, n_elems-1)
        print(f"2. Adding a new element {x_n:g} at {x_n_place}")
        seq.insert(x_n_place, x_n)
        print(f"2. Now seq[{x_n_place}] is {seq[x_n_place]:g}")

    if choice == 3:
        x_n_place = randint(0, n_elems-1)
        print(f"3. Deleting {x_n_place}'th element from seq")
        seq.pop(x_n_place)
        print(f"3. now seq[{x_n_place}] is {seq[x_n_place]:g}")
    if choice == 4:
        print("4. Clearing the list")
        seq.clear()
        print(f"4. Now seq is {seq}")
    if choice == 5:


        k = int(input(">>> number k of k'th extremum in list (int+): "))
        assert k > 0
        if n < 2:
            print("Can't find an extremum in an list, len<2")

        n_extremum = 0
        for i in range(1,n-1):
            if seq[i-1] > seq[i] < seq[i+1]: # minima
                n_extremum += 1
            elif seq[i-1] < seq[i] > seq[i+1]: # maxima
                n_extremum += 1
            if n_extremum == k:
                print(f"{k}'th extremum is {seq[i]}")
                break
            if i == n-2:
                print(f"No {k}'th extremum found")

    if choice == 8:
        print("Sir, I shall enquire thou to input a list thee desireth")
        n = int(input(">>> n_elems in your list (int+): "))
        seq = [0] * n

        # read seq
        for i in range(n):
            seq[i] = float(input(f">>> seq[{i}]= "))

