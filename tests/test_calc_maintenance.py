# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib
import os

import pytest  # noqa: I900


class TestClassMaintenance():

    def _run(self, in_, *args):
        from multimetric.__main__ import parse_args
        from multimetric.__main__ import run

        file = in_

        if isinstance(file, str):
            file = [file]

        args_ = parse_args(list(args) + file)
        loc = []
        for f in file:
            with open(f) as i:
                loc.append(sum(1 for x in i.read() if x == '\n'))
        return (run(args_), file, loc)
    
    def test_maintenance_default(self):
        file = os.path.join(pytest.test_dir_local, 'test.c')

        res, _, _ = self._run(file)

        assert res.get('files', {}).get(file, {}).get('maintainability_index', 0) == 82.204

    def test_maintenance_sei(self):
        file = os.path.join(pytest.test_dir_local, 'test.c')

        res, _, _ = self._run(file, '--maintindex', 'sei')

        assert res.get('files', {}).get(file, {}).get('maintainability_index', 0) == 125.979

    def test_maintenance_classic(self):
        file = os.path.join(pytest.test_dir_local, 'test.c')

        res, _, _ = self._run(file, '--maintindex', 'classic')

        assert res.get('files', {}).get(file, {}).get('maintainability_index', 0) == 82.204

    def test_maintenance_microsoft(self):
        file = os.path.join(pytest.test_dir_local, 'test.c')

        res, _, _ = self._run(file, '--maintindex', 'microsoft')

        assert res.get('files', {}).get(file, {}).get('maintainability_index', 0) == 48.072


