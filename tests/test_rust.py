# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib
import os

import pytest  # noqa: I900


class TestClassRust():

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
    
    def test_rust(self):
        file = os.path.join(pytest.test_dir_local, 'test.rs')

        res, _, _ = self._run(file)

        assert 'Rust' in res.get('files', {}).get(file, {}).get('lang', [])
        assert res.get('files', {}).get(file, {}).get('comment_ratio', 0) == 10.024
        assert res.get('files', {}).get(file, {}).get('cyclomatic_complexity', 0) == 4
        assert res.get('files', {}).get(file, {}).get('fanout_external', 0) == 3
        assert res.get('files', {}).get(file, {}).get('fanout_internal', 0) == 0
        assert res.get('files', {}).get(file, {}).get('halstead_bugprop', 0) == 0.504
        assert res.get('files', {}).get(file, {}).get('halstead_difficulty', 0) == 29.934
        assert res.get('files', {}).get(file, {}).get('halstead_effort', 0) == 45268.064
        assert res.get('files', {}).get(file, {}).get('halstead_timerequired', 0) == 2514.892
        assert res.get('files', {}).get(file, {}).get('halstead_volume', 0) == 1512.252
        assert res.get('files', {}).get(file, {}).get('loc', 0) == 42
        assert res.get('files', {}).get(file, {}).get('maintainability_index', 0) == 71.459
        assert res.get('files', {}).get(file, {}).get('operands_sum', 0) == 91
        assert res.get('files', {}).get(file, {}).get('operands_uniq', 0) == 38
        assert res.get('files', {}).get(file, {}).get('operators_sum', 0) == 162
        assert res.get('files', {}).get(file, {}).get('operators_uniq', 0) == 25
        assert res.get('files', {}).get(file, {}).get('pylint', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe', 0) == 93.807
        assert res.get('files', {}).get(file, {}).get('tiobe_compiler', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_complexity', 0) == 58.716
        assert res.get('files', {}).get(file, {}).get('tiobe_coverage', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_duplication', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_fanout', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_functional', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_security', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_standard', 0) == 100.0
