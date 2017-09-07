# coding=utf-8
"""Creates a static HTML Page containing a DGGS Implementation Matrix to display
via github-pages."""
import os

import markdown
from tabulate import tabulate
import yaml

DIR_DATA = 'data'
DIR_DOCS = 'docs'
DIR_RES = 'res'
FILE_FOOT = 'foot.html'
FILE_HEAD = 'head.html'
FILE_HEADERS = 'requirements.yaml'
FILE_INDEX = 'index.html'
FILE_SCRIPT = 'script.js'
MD_EXTENSIONS = ['markdown.extensions.tables']
TABLE_FORMAT = 'pipe'
WRITE = 'w+'
YAML = '.yaml'


def generate_table_column_headers():
    """Generate column headers for the DGGS Compliance Matrix table from the
    .yaml files found in the ../res directory."""
    res = os.path.join(os.path.pardir, DIR_RES)
    header_stream = open(os.path.join(res, FILE_HEADERS))
    with header_stream:
        headers = yaml.load(header_stream, yaml.Loader)
    yield from headers


def generate_table_rows():
    """Generate rows for the DGGS Compliance Matrix table from the .yaml files
    found in the ../data directory."""
    data = os.path.join(os.path.pardir, DIR_DATA)
    filenames = [path for path in os.listdir(data) if path.endswith(YAML)]
    file_paths = [os.path.join(data, filename) for filename in filenames]
    data_streams = [open(data) for data in file_paths]
    rows = []
    for data_stream in data_streams:
        with data_stream:
            rows.append(yaml.load(data_stream, yaml.Loader))
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
    _docs_path = os.path.join(_pwd, DOCS_DIR)
    _output_file = os.path.join(_docs_path, INDEX_FILE)
    _output_stream = open(_output_file, WRITE)
    with _output_stream:
        _output_stream.writelines(_raw_html)


def main():
    """Verifies all necessary files are present to build successfully. If not,
    notify the user with an informative help message. If so write the index.html
    files in ../docs."""

if __name__ is '__main__':
    main()
