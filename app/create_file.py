import os
import datetime


def create_file(arguments: list) -> None:
    if "-d" in arguments and "-f" in arguments:
        path = define_directories(arguments)
        make_directories(path)
        file_name = define_file_name(arguments)
        add_information_in_file(os.path.join(path, file_name))
    elif "-d" in arguments:
        path = define_directories(arguments)
        make_directories(path)
    elif "-f" in arguments:
        file_name = define_file_name(arguments)
        add_information_in_file(file_name)


def make_directories(*args) -> None:
    current_directory = os.getcwd()
    new_directory = os.path.join(*args)
    path = os.path.join(current_directory, new_directory)

    try:
        os.makedirs(path, exist_ok=False)
        print(f"Directory {new_directory} created successfully")
    except OSError:
        print("Directory '%s' can not be created" % new_directory)


def define_file_name(arguments: list) -> str:
    # a = "python create_file.py -d dir1 dir2 -f file.txt".split()
    return " ".join(arguments[arguments.index("-f") + 1:])


def define_directories(arguments: list) -> str:
    if "-f" in arguments:
        index_d = arguments.index("-d")
        index_f = arguments.index("-f")
        return " ".join(arguments[index_d + 1: index_f])
    return " ".join(arguments[arguments.index("-d") + 1:])


def add_information_in_file(file_name: str) -> None:
    lines_arr = []
    while True:
        new_string = input("Enter new line of content: ")
        if new_string != "stop":
            lines_arr.append(new_string)
        else:
            break
    with open(file_name, "a") as file:
        current_time = datetime.datetime.now()
        file.write(current_time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for line in lines_arr:
            file.write(f"{line}\n")
