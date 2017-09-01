#!/usr/bin/env python
# all the import
import sys, os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_DIR)

from mycv.application import app

if __name__ == '__main__':
    app.run(host='127.0.0.1',
            debug=True,
            port=5555)

# package
# module
# instance