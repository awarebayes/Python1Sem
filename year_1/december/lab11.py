"""
Лабораторная работа № 11
Имитировать работу базы данных, используя бинарный файл.
Запись содержит 3-4 поля. Например, запись "книга" содержит поля "автор", "наименование", "год издания".
Необходимо сделать меню:
1. Создание БД.
2. Добавление записи в БД.
3. Вывод всей БД.
4. Поиск записи по одному полю.
5. Поиск записи по двум полям.
Для работы с текущей записью используется словарь.
# Написал Щербина МА ИУ7-15б
"""

import pickle
import os
import pprint

name_to_type = dict([(t.__name__, t) for t in [int, float, str]])
pp = pprint.PrettyPrinter(indent=4, depth=10)

# loop over objects in file
def iter_objects(db_file_path):
    with open(db_file_path, "rb") as f:
        while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break

# ask where db file should be located
def ask_file_dir():
    name = input(">>> file_name, default=db.pkl: ")
    path = input(f">>> path, default={os.getcwd() +'/'}): ")
    if not path: # default path is getcwd
        path = os.getcwd() + "/"
    if not name: # default name is db.pkl
        name = "db.pkl"
    db_file_path = path + name
    if os.path.exists(db_file_path): # Ask whether should reinit if present
        should_reinit = ask_yes_no("File is already present. Reinitialize the db?")
        if should_reinit:
            with open(db_file_path, "wb") as f:
                pass
    return db_file_path

# ask yes or no? Yes?
def ask_yes_no(prompt):
    option = ""
    while option not in ["y", "n"]:
        option = input(prompt + " (y/n) ")
    return option == "y"


# Recursively generate a new record
def gen_record(result=None, outer_name="root"):
    if result is None: # beware of default mutability!
        result = dict()
    print(f"\n{outer_name}")
    print("Creating a new field...")
    name_str = input(">>> name: ")
    is_nested = ask_yes_no("Is this field nested?")
    if not is_nested:
        type_str = input(">>> type: ")
        value_str = input(">>> value: ")
        # type conversion
        if type != str:
            value = name_to_type[type_str](value_str)
        else:
            value = value_str
    else: # is nested, call recursion
        value = gen_record(outer_name=f"{outer_name} -> " + name_str)
    result[name_str] = value
    should_continue = ask_yes_no("\nAdd more fields? We are in " + outer_name)
    if should_continue:
        return gen_record(result, outer_name)
    print("Generated record:")
    pp.pprint(result)
    return result

# dump object to file, default is append
def dump_to_file(obj, db_file_path):
    with open(db_file_path, "ab") as f:
        pickle.dump(obj, f)

# partial equality for comparison
def partial_eq(child, parent):
    # check keys first
    if not set(child.keys()) <= set(parent.keys()):
        return False
    # check values later
    for key in child.keys():
        if isinstance(child[key], dict): # nested record
            if not partial_eq(child[key], parent[key]):
                return False
        else: # non-nested record
            if child[key] != parent[key] and type(child[key]) != type(parent[key]):
                return False
    return True


def main():
    db_file_path = "/home/mike/Documents/uni/db.pkl"
    while True:
        print(
            """
        1. Создание БД.
        2. Добавление записи в БД.
        3. Вывод всей БД.
        4. Поиск записи.
        5. Выйти
        """
        )
        option = int(input(">>> option: "))
        if option == 1: # db_file_path reinit
            db_file_path = ask_file_dir()
        if option == 2: # generate new record
            dump_to_file(gen_record(), db_file_path)
        if option == 3: # loop over objects
            for obj in iter_objects(db_file_path):
                pp.pprint(obj)
        if option == 4: # search
            target = gen_record()
            print("\nSearching...")
            for obj in filter(
                lambda x: partial_eq(target, x),
                iter_objects(db_file_path)
            ):
                pp.pprint(obj)
            print("Objects ended!")
        if option == 5: # exit
            exit(0)


if __name__ == "__main__":
    main()
