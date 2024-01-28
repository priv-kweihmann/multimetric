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
    
    def test_maintenance_individual_classic(self):
        file = os.path.join(pytest.test_dir_local, 'test.c')

        res, _, _ = self._run(file, '--maintindex', 'individual')

        assert res.get('files', {}).get(file, {}).get('maintainability_index', 0) == 82.204

    def test_maintenance_individual(self):
        file = os.path.join(pytest.test_dir_local, 'test.c')

        res, _, _ = self._run(file, '--maintindex', 'individual','--maintindex-formula','max(0,171.0 - 5.2 * math.log(halstead_volume) - 0.23* cyclomatic_complexity -16.2 * math.log(loc)) + math.sin(math.sqrt(2.4*comment_ratio/100.0))')

        assert res.get('files', {}).get(file, {}).get('maintainability_index', 0) == 82.612



