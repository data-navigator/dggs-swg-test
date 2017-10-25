# coding=utf-8
"""Creates a static HTML Page containing a DGGS Implementation Matrix to display
via github-pages."""
import os

import markdown
from tabulate import tabulate
import yaml

ANCHOR_LINK = '#requirement_'
DIR_DATA = 'data'
DIR_DOCS = 'docs'
DIR_RES = 'res'
DOC_URL = 'http://docs.opengeospatial.org/as/15-104r5/15-104r5.html'
FILE_FOOT = 'foot.html'
FILE_HEAD = 'head.html'
FILE_HEADERS = 'requirements.yaml'
FILE_INDEX = 'index.html'
FILE_SCRIPT = 'script.js'
MD_EXTENSIONS = ['markdown.extensions.tables']
TABLE_FORMAT = 'pipe'
TABLE_TAG = '<table>'
TABLE_ID_TAG = '<table id="dggs-matrix" class="display">'
WRITE = 'w+'
YAML = '.yaml'


def generate_table_rows():
    """Generate row values for the DGGS Compliance Matrix table from the
    .yaml files found in the ../res directory."""
    res = os.path.join(os.path.pardir, DIR_RES)
    requirements_stream = open(os.path.join(res, 'en', FILE_HEADERS))
    with requirements_stream:
        # list of dictionaries
        requirements = yaml.load(requirements_stream, yaml.Loader)
    data = os.path.join(os.path.pardir, DIR_DATA)
    file_names = [path for path in os.listdir(data) if path.endswith(YAML)]
    file_paths = [os.path.join(data, file_name) for file_name in file_names]
    data_streams = [open(data) for data in file_paths]
    rows = []
    for data_stream in data_streams:
        with data_stream:
            yaml_data = yaml.load(data_stream, yaml.Loader)
            results = yaml_data['requirements']
            rows.append([parse_result(r) for r in results])
    yield from zip([parse_requirement(r) for r in requirements], *rows)


def parse_requirement(requirement):
    """Turns a requirement from a dictionary into html string."""
    name = requirement['name']
    title = requirement['title']
    url = DOC_URL + ANCHOR_LINK + str(requirement['requirement'])
    link = f'<a href={url}>{name}</a>'
    return f'<span title="{title}">{link}</span>'


def parse_result(result):
    """Turns a result from a scalar into a html string."""
    return f'<span title="{str(result)}">{str(result)}</span>'


def generate_table_column_headers():
    """Generate column headers for the DGGS Compliance Matrix table from the
    names of implementations defined in the .yaml files found in the ../data
    directory."""
    data = os.path.join(os.path.pardir, DIR_DATA)
    file_names = [path for path in os.listdir(data) if path.endswith(YAML)]
    file_paths = [os.path.join(data, file_name) for file_name in file_names]
    data_streams = [open(data) for data in file_paths]
    rows = []
    for data_stream in data_streams:
        with data_stream:
            yaml_data = yaml.load(data_stream, yaml.Loader)
            url = yaml_data['url']
            tag_open = f'<a href="{url}">'
            tag_close = '</a>'
            rows.append(tag_open + yaml_data['name'] + tag_close)
    yield from rows


def create_table_html():
    """Create the html table to embed in the body of index.html"""
    rows = generate_table_rows()
    cols = generate_table_column_headers()
    table = tabulate(rows, cols, tablefmt=TABLE_FORMAT)
    return markdown.markdown(table, extensions=MD_EXTENSIONS)


def create_index_html():
    """Create the html for the index file in the ../docs directory which will be
    served on github-pages."""
    head = open(FILE_HEAD)
    body = create_table_html().replace(TABLE_TAG, TABLE_ID_TAG)
    foot = open(FILE_FOOT)
    with head, foot:
        return ''.join([head.read(), body, foot.read()])


def main():
    """Verifies all necessary files are present to build successfully. If not,
    notify the user with an informative help message. If so write the index.html
    files in ../docs."""
    html = create_index_html()
    path = os.path.join(os.path.pardir, DIR_DOCS, FILE_INDEX)
    with open(path, WRITE) as output_stream:
        output_stream.writelines(html)

if __name__ == '__main__':
    print('Creating index.html')
    main()
