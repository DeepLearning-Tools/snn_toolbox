from __future__ import absolute_import, print_function
import os

_base_dir = os.path.expanduser('~')
if not os.access(_base_dir, os.W_OK):
    _base_dir = '/tmp'

_dir = os.path.join(_base_dir, '.snntoolbox')
if not os.path.exists(_dir):
    os.makedirs(_dir)

_config_path = os.path.join(_dir, 'preferences')
if not os.path.exists(_config_path):
    os.makedirs(_config_path)

# python 2 can not handle the 'flush' keyword argument of python 3 print().
# Provide 'echo' function as an alias for
# "print with flush and without newline".
try:
    from functools import partial
    echo = partial(print, end='', flush=True)
    echo(u'')
except TypeError:
    # TypeError: 'flush' is an invalid keyword argument for this function
    import sys

    def echo(text):
        """python 2 version of print(end='', flush=True)."""
        sys.stdout.write(u'{0}'.format(text))
        sys.stdout.flush()