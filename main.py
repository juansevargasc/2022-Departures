import os


def run_example():
    a = 'Run this example'
    b = os.path.abspath('./')
    print('{} - This is the path: {}'.format(a, b))


run_example()
