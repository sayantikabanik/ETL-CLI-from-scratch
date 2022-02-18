"""
Simple demo for nested tasks
(can be more complicated)

The dependent files for one block of tasks, should be same
or try passing multiple dependent files in loop

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
