"""
Task and action setup to write some values to a file
cmd to run: <doit>
"""


def task_hello():
    """hello"""

    def python_hello(targets):
        with open(targets[0], "a") as output:
            output.write("Python says Hello World!!!\n")

    return {
        'actions': [python_hello],
        'targets': ["output/hello.txt"],
        }
