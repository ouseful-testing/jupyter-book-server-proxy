"""
Return config on servers to start for jupyter_book_server_proxy
See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""

__version__="0.0.1"

import os
import pkg_resources

def setup_jupyter_book():
    fpath = pkg_resources.resource_filename('jupyter_book_server_proxy', 'static/')
    return {
        'command': ["python3", "-m", "http.server", "--directory", fpath, "{port}"],
        'environment': {},
        'launcher_entry': {
            'title': 'Jupyter Book',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'jupyter_book.svg')
        }
    }
