# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib
import os

import pytest  # noqa: I900


class TestClassPHP():

    def _run(self, in_):
        from multimetric.__main__ import parse_args
        from multimetric.__main__ import run

        file = in_

        if isinstance(file, str):
            file = [file]

        args_ = parse_args(file)
        loc = []
        for f in file:
            with open(f) as i:
                loc.append(sum(1 for x in i.read() if x == '\n'))
        return (run(args_), file, loc)
    
    def test_php(self):
        file = os.path.join(pytest.test_dir_local, 'test.php')

        res, _, _ = self._run(file)

        assert 'PHP' in res.get('files', {}).get(file, {}).get('lang', [])
        assert res.get('files', {}).get(file, {}).get('comment_ratio', 0) == 6.542
        assert res.get('files', {}).get(file, {}).get('cyclomatic_complexity', 0) == 5
        assert res.get('files', {}).get(file, {}).get('fanout_external', 0) == 3
        assert res.get('files', {}).get(file, {}).get('fanout_internal', 0) == 0
        assert res.get('files', {}).get(file, {}).get('halstead_bugprop', 0) == 0.09
        assert res.get('files', {}).get(file, {}).get('halstead_difficulty', 0) == 15.0
        assert res.get('files', {}).get(file, {}).get('halstead_effort', 0) == 4065.429
        assert res.get('files', {}).get(file, {}).get('halstead_timerequired', 0) == 225.857
        assert res.get('files', {}).get(file, {}).get('halstead_volume', 0) == 271.029
        assert res.get('files', {}).get(file, {}).get('loc', 0) == 16
        assert res.get('files', {}).get(file, {}).get('maintainability_index', 0) == 100
        assert res.get('files', {}).get(file, {}).get('operands_sum', 0) == 24
        assert res.get('files', {}).get(file, {}).get('operands_uniq', 0) == 12
        assert res.get('files', {}).get(file, {}).get('operators_sum', 0) == 33
        assert res.get('files', {}).get(file, {}).get('operators_uniq', 0) == 15
        assert res.get('files', {}).get(file, {}).get('pylint', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe', 0) == 91.0
        assert res.get('files', {}).get(file, {}).get('tiobe_compiler', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_complexity', 0) == 40.0
        assert res.get('files', {}).get(file, {}).get('tiobe_coverage', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_duplication', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_fanout', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_functional', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_security', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_standard', 0) == 100.0
