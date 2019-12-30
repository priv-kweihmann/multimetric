#!/bin/sh
python3 setup.py build
python3 setup.py sdist
./test.sh || exit 1
twine upload dist/*