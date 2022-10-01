import re
import sys

plugin_id = '{{cookiecutter.plugin_id}}'

print(sys.version_info)

if sys.version_info < (3, 8):
    print('ERROR: Python >= 3.8 needed.')
    sys.exit(1)

if not re.match('^[a-zA-z][a-zA-Z0-9_]*$', plugin_id):
    print('ERROR: Plugin ID should consist of alphanumeric characters and underscores, and should not start with a number.')
    sys.exit(1)