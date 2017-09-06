import io
import os
from tabulate import tabulate
import yaml

DATA_PATH = os.path.join('.', '_data')
HEADERS_FILE = 'headers.yaml'
YAML = '.yaml'

try:
    _headers_stream = open(HEADERS_FILE)
    _walk = [path for path in os.listdir(DATA_PATH) if path.endswith(YAML)]
    _data_files = [os.path.join(DATA_PATH, path) for path in _walk]
    _dggs_data = [open(data) for data in _data_files]
except IOError:
    raise

with _headers_stream:
    _headers = [h for h in yaml.load(_headers_stream, yaml.Loader)]

_tabular_data = []
for _implementation in _dggs_data:
    with _implementation:
        _tabular_data.append(yaml.load(_implementation))

_output = tabulate(tabular_data=list(_tabular_data), headers=_headers)
print(_output)
