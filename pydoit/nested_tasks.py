"""
Simple demo for nested tasks
(can be more complicated)

The dependent files for each block of nested tasks, 
could be same or a list of files

The 'name' param should be unique
The method names should always start with "task_"
"""


def task_create():
    return {'actions': ["touch output/nested.txt"],
            'targets': ["output/nested.txt"]
            }


def task_some_action():
    task_list = ["cd output/", "echo testing_nested > output/nested.txt"]
    for task_ in task_list:
        task_name = "task:" + task_.split(' ')[0]
        yield{'name': task_name,
              'actions': [task_],
              'file_dep': ["output/nested.txt"]
              }
