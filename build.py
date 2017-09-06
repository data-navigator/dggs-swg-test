import io
import os
from tabulate import tabulate
import yaml

DATA_PATH = os.path.join('.', '_data')
HEADERS_FILE = 'headers.yaml'

_errors = io.StringIO()

try:
    _headers_stream = open(HEADERS_FILE)
    _walk = [path for path in os.listdir(DATA_PATH) if path.endswith('.yaml')]
    _data_files = [os.path.join(DATA_PATH, path) for path in _walk]
    _dggs_data = [open(data) for data in _data_files]
    _output_file = open('test.txt', 'w+')
except IOError as _io_error:
    _errors.write(str(_io_error))

with _headers_stream:
    _headers = [h for h in yaml.load(_headers_stream, yaml.Loader)]

_tabular_data = []
for _implementation in _dggs_data:
    with _implementation:
        _tabular_data.append(yaml.load(_implementation))

_output = tabulate(tabular_data=list(_tabular_data), headers=_headers)
print(_output)

with _output_file:
    _output_file.write(_output)

if len(_errors.getvalue()):
    print(_errors.getvalue())
