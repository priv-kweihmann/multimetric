#! /bin/bash
export PATH=$(pwd)/bin:${PATH}
for _test in $(pwd)/tests/*.test; do
    /bin/bash ${_test} || true
done