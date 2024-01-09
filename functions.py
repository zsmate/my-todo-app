FILENAME = "todos.txt"
def read_todos(filename=FILENAME):
    """ Read the text file and return todos."""
    with open(filename, "r") as file:
        todos = file.readlines()
    return todos

# print(help(read_todos))
def write_todos(todos_arg, filename=FILENAME):
    with open(filename, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print(read_todos())