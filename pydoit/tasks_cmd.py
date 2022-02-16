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
