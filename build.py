# coding=utf-8
"""Generate a HTML Page containing a DGGS Implementation Matrix to display via github-pages."""
import io
import os
from tabulate import tabulate
import yaml

DATA_DIR =  '_data'
HEADERS_FILE = 'headers.yaml'
YAML = '.yaml'

_Loader = yaml.Loader
_data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), DATA_DIR)
_headers_stream = open(HEADERS_FILE)
_files = [path for path in os.listdir(_data_path) if path.endswith(YAML)]
_file_paths = [os.path.join(_data_path, path) for path in _files]
_dggs_data_streams = [open(data) for data in _file_paths]
_dggs_table = []

with _headers_stream:
    _header_yaml = yaml.load(stream=_headers_stream, Loader=_Loader)
    _headers = [header for header in _header_yaml]
for _dggs_data_stream in _dggs_data_streams:
    with _dggs_data_stream:
        _dggs_table.append(yaml.load(stream=_dggs_data_stream, Loader=_Loader))
_output = tabulate(tabular_data=_dggs_table, headers=_headers)
print(_output)
