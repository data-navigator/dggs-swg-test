# coding=utf-8
"""Generate a HTML Page containing a DGGS Implementation Matrix to display via github-pages."""
import os
import pprint

import markdown
from tabulate import tabulate
import yaml

BODY = '<body>'
BODY_CLOSE = '</body>'
CSS = '<link rel="stylesheet" href="style.css">'
DATA_DIR =  '_data'
DOCS_DIR = 'docs'
DOCTYPE = '<!DOCTYPE html>'
FORMAT = 'pipe'
JS_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'
SCRIPT = '<script src="{}"></script>'
HEADERS_FILE = 'headers.yaml'
HEAD = '<head>'
HEAD_CLOSE = '</head>'
HTML = '<html>'
HTML_CLOSE = '</html>'
INDEX_FILE = 'index.html'
MD_TABLES_EXTENSION = 'markdown.extensions.tables'
SCRIPT_FILE = 'script.js'
TABLE_DIR = '_table'
YAML = '.yaml'
WRITE = 'w+'

_pwd = os.path.dirname(os.path.realpath(__file__))
_table_path = os.path.join(_pwd, TABLE_DIR)
_headers_stream = open(os.path.join(_table_path, HEADERS_FILE))
with _headers_stream:
    _header_yaml = yaml.load(_headers_stream, yaml.Loader)
    _headers = [header for header in _header_yaml]
_data_path = os.path.join(_pwd, DATA_DIR)
_files = [path for path in os.listdir(_data_path) if path.endswith(YAML)]
_file_paths = [os.path.join(_data_path, path) for path in _files]
_dggs_data_streams = [open(data) for data in _file_paths]
_dggs_table = []
for _dggs_data_stream in _dggs_data_streams:
    with _dggs_data_stream:
        _dggs_table.append(yaml.load(_dggs_data_stream, yaml.Loader))
_jquery = SCRIPT.format(JS_URL))
_script = SCRIPT.format(os.path.join(DOCS_DIR, SCRIPT_FILE))
_lead_tags = [DOCTYPE, HTML, HEAD, CSS, _jquery, _script, HEAD_CLOSE, BODY]
_table = tabulate(_dggs_table, _headers, tablefmt=FORMAT)
_body = markdown.markdown(_table, extensions=[MD_TABLES_EXTENSION])
_end_tags = [BODY_CLOSE, HTML_CLOSE]
_raw_html = '\n'.join(_lead_tags + [_body] + _end_tags)
_docs_path = os.path.join(_pwd, DOCS_DIR)
_output_file = os.path.join(_docs_path, INDEX_FILE)
_output_stream = open(_output_file, WRITE)
with _output_stream:
    _output_stream.writelines(_raw_html)
