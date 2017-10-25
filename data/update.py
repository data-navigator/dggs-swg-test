# coding=utf-8
"""Update values in dummy files"""
import os
import random
import yaml


def run(requirement):
    r = 'true' in requirement.lower()
    result = str(random.randint(1, 10) if r else 0) + '/10'
    return(result)


yamls = [y for y in os.listdir() if 'yaml' in y]
for y in yamls:
    with open(y) as read:
        data = yaml.load(read, yaml.Loader)
        requirements = data['requirements'].split(' ')
        update = [run(requirement) for requirement in requirements]
        data['requirements'] = update
    with open(y, "w+") as write:
        yaml.dump(data, write)
