# coding=utf-8
"""Generate a HTML Page containing a DGGS Implementation Matrix to display via github-pages."""
import io
import os
from tabulate import tabulate
import yaml

DATA_PATH = os.path.join('.', '_data')
HEADERS_FILE = 'headers.yaml'
YAML = '.yaml'

_Loader = yaml.Loader
_headers_stream = open(HEADERS_FILE)
_files = [path for path in os.listdir(DATA_PATH) if path.endswith(YAML)]
_file_paths = [os.path.join(DATA_PATH, path) for path in _files]
_dggs_data_streams = [open(data) for data in _file_paths]

with _headers_stream:
    _header_yaml = yaml.load(stream=_headers_stream, Loader=_Loader)
    _headers = [header for header in _header_yaml]

_dggs_table = []
for _dggs_data_stream in _dggs_data_streams:
    with _dggs_data_stream:
        _dggs_table.append(yaml.load(stream=_dggs_data_stream, Loader=_Loader))

_output = tabulate(tabular_data=_dggs_table, headers=_headers)
print(_output)
