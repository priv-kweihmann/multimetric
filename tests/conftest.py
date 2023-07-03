# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib

import os
import zipfile
import tempfile
import shutil
import glob

import pytest
import requests

# For testing we are using the awesome collection from
# https://github.com/TheRenegadeCoder/sample-programs
# MIT License
#
# Copyright (c) 2018 Jeremy Grifski
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
SAMPLE_PROGRAMS_REVISION = "c25d61bcf10e04282ab53a5a5a4480b463a2db8e"
SAMPLE_PROGRAMS_URL = f"https://github.com/TheRenegadeCoder/sample-programs/archive/{SAMPLE_PROGRAMS_REVISION}.zip"


def pytest_sessionstart(session):
    pytest.test_dir = os.path.join(os.path.dirname(__file__), '__data')
    pytest.test_dir_local = os.path.join(os.path.dirname(__file__), '__data_local')
    pytest.test_dir_samples = os.path.join(pytest.test_dir, f'sample-programs-{SAMPLE_PROGRAMS_REVISION}')
    if os.path.exists(pytest.test_dir):
        return
    os.makedirs(pytest.test_dir, exist_ok=True)
    # download the archive
    req = requests.get(SAMPLE_PROGRAMS_URL, allow_redirects=True)
    with tempfile.NamedTemporaryFile(mode='wb') as o:
        o.write(req.content)
        o.flush()
        # unpack it
        with zipfile.ZipFile(o.name) as z:
            z.extractall(pytest.test_dir)

def pytest_generate_tests(metafunc):
    file_map = {}
    _map = {
        'file_BASH': 'archive/b/bash',
        'file_C': 'archive/c/c',
        'file_COFFEESCRIPT': 'archive/c/coffeescript',
        'file_CPP': 'archive/c/c-plus-plus',
        'file_CSHARP': 'archive/c/c-sharp',
        'file_DART': 'archive/d/dart',
        'file_GO': 'archive/g/go',
        'file_GROOVY': 'archive/g/groovy',
        'file_HASKELL': 'archive/h/haskell',
        'file_JAVA': 'archive/j/java',
        'file_JAVASCRIPT': 'archive/j/javascript',
        'file_JULIA': 'archive/j/julia',
        'file_KOTLIN': 'archive/k/kotlin',
        'file_LISP': 'archive/l/lisp',
        'file_LUA': 'archive/l/lua',
        'file_OBJECTIVEC': 'archive/o/objective-c',
        'file_PERL': 'archive/p/perl',
        'file_PHP': 'archive/p/php',
        'file_PYTHON': 'archive/p/python',
        'file_RUBY': 'archive/r/ruby',
        'file_RUST': 'archive/r/rust',
        'file_TCL': 'archive/t/tcl',
        'file_TYPESCRIPT': 'archive/t/typescript',
        'file_ZIG': 'archive/z/zig',
    }

    def get_files(dir):
        res = []
        for root, _, files in os.walk(dir):
            for f in files:
                if f in ['testinfo.yml', 'README.md']:
                    continue
                res.append(os.path.join(root, f))
        return res

    for k, v in _map.items():
        file_map[k] = get_files(os.path.join(pytest.test_dir_samples, v))

    matching_keys = [x for x in metafunc.fixturenames if x in file_map.keys()]
    for m in matching_keys:
        metafunc.parametrize(m, file_map[m])

def pytest_sessionfinish(session, exitstatus):
    #shutil.rmtree(pytest.test_dir, ignore_errors=True)
    pass
