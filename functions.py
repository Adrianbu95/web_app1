FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do list in the text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


""" It is used to control when the file is import or when the file is directly
 executed. When functions.py are executed, variable __name__ is equal to __name__ 
 but when is indirectly executed by import in cli.py the value of __name__ is 
 the name of the file, in that case __functions__
"""
if __name__ == "__main__":
    print("Hello")
    print(get_todos())