# coding: utf-8
"""Create multiple .yaml files containing dummy data for display on the OGC DGGS
Matrix site."""
import os
import random


def create_file_stream(filename):
    """Create a trucate and write file stream in this file's folder for a given
    filename."""
    pwd = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(pwd, '.'.join([filename, 'yaml']))
    return open(filepath, 'w+')


def create_dummy_yaml(implementation_name):
    """Create the yaml string to write to a dummy DGGS .yaml file."""
    random_vals = ['- ' + str(random.randint(0, 10) % 2 == 0) for _ in range(18)]
    return '\n'.join([implementation_name] + random_vals)


def main(name_list):
    """Execute the creation of dummy yaml files for each given name in a list."""
    for name in name_list:
        with create_file_stream(name) as stream:
            stream.write('- ' + create_dummy_yaml(name))

if __name__ == '__main__':
    main(['OneFish', 'TwoFish', 'RedFish', 'BlueFish', 'Thing1', 'Thing2',
          'CatInHat'])
