"""
Multiple tasks with sequential dependency
cmd to run: <doit -f tasks_cmd.py>
"""


def task_create():
    return {'actions': ["touch output/foo.txt"],
            'targets': ["output/foo.txt"]
            }


def task_modify():
    return {'actions': ["echo testing_write > output/foo.txt"],
            'file_dep': ["output/foo.txt"]
            }


"""
nested version
"""


def task_test():
    name_file = input("Enter filename")
    task_list = ["touch output/{}".format(name_file), "echo testing_write_123 > output/{}".format(name_file)]
    for task_ in task_list:
        task_name = task_.split(' ')[1]
        yield{'name': task_name,
              'doc': 'initial test task',
              'actions': [task_],
              'file_dep': ["output/foo.txt"]
              }
