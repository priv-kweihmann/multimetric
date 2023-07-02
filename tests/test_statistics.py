# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib
import os
import statistics

import pytest  # noqa: I900


class TestClassStatistics():

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
    
    def test_stats_overall(self):
        files = [
                os.path.join(pytest.test_dir_samples, 'archive/c/c/baklava.c'),
                os.path.join(pytest.test_dir_samples, 'archive/c/c-plus-plus/bubble-sort.cpp')
        ]
        res, _, _ = self._run(files)

        assert res.get('overall', {}).get('loc', 0) == sum(v.get('loc', 0) for k, v in res.get('files', {}).items())
        assert res.get('overall', {}).get('operands_sum', 0) == sum(v.get('operands_sum', 0) for k, v in res.get('files', {}).items())
        assert res.get('overall', {}).get('operators_sum', 0) == sum(v.get('operators_sum', 0) for k, v in res.get('files', {}).items())
    
    def test_stats_min(self):
        files = [
                os.path.join(pytest.test_dir_samples, 'archive/c/c/baklava.c'),
                os.path.join(pytest.test_dir_samples, 'archive/c/c-plus-plus/bubble-sort.cpp')
        ]
        res, _, _ = self._run(files)

        assert res.get('stats', {}).get('min', {}).get('loc', 0) == min(v.get('loc', 0) for k, v in res.get('files', {}).items())
        assert res.get('stats', {}).get('min', {}).get('operands_sum', 0) == min(v.get('operands_sum', 0) for k, v in res.get('files', {}).items())
        assert res.get('stats', {}).get('min', {}).get('operators_sum', 0) == min(v.get('operators_sum', 0) for k, v in res.get('files', {}).items())

    def test_stats_max(self):
        files = [
                os.path.join(pytest.test_dir_samples, 'archive/c/c/baklava.c'),
                os.path.join(pytest.test_dir_samples, 'archive/c/c-plus-plus/bubble-sort.cpp')
        ]
        res, _, _ = self._run(files)

        assert res.get('stats', {}).get('max', {}).get('loc', 0) == max(v.get('loc', 0) for k, v in res.get('files', {}).items())
        assert res.get('stats', {}).get('max', {}).get('operands_sum', 0) == max(v.get('operands_sum', 0) for k, v in res.get('files', {}).items())
        assert res.get('stats', {}).get('max', {}).get('operators_sum', 0) == max(v.get('operators_sum', 0) for k, v in res.get('files', {}).items())

    def test_stats_mean(self):
        files = [
                os.path.join(pytest.test_dir_samples, 'archive/c/c/baklava.c'),
                os.path.join(pytest.test_dir_samples, 'archive/c/c-plus-plus/bubble-sort.cpp')
        ]
        res, _, _ = self._run(files)

        assert res.get('stats', {}).get('mean', {}).get('loc', 0) == statistics.mean(v.get('loc', 0) for k, v in res.get('files', {}).items())
        assert res.get('stats', {}).get('mean', {}).get('operands_sum', 0) == statistics.mean(v.get('operands_sum', 0) for k, v in res.get('files', {}).items())
        assert res.get('stats', {}).get('mean', {}).get('operators_sum', 0) == statistics.mean(v.get('operators_sum', 0) for k, v in res.get('files', {}).items())

    def test_stats_median(self):
        files = [
                os.path.join(pytest.test_dir_samples, 'archive/c/c/baklava.c'),
                os.path.join(pytest.test_dir_samples, 'archive/c/c-plus-plus/bubble-sort.cpp')
        ]
        res, _, _ = self._run(files)

        assert res.get('stats', {}).get('mean', {}).get('loc', 0) == statistics.median(v.get('loc', 0) for k, v in res.get('files', {}).items())
        assert res.get('stats', {}).get('mean', {}).get('operands_sum', 0) == statistics.median(v.get('operands_sum', 0) for k, v in res.get('files', {}).items())
        assert res.get('stats', {}).get('mean', {}).get('operators_sum', 0) == statistics.median(v.get('operators_sum', 0) for k, v in res.get('files', {}).items())

    def test_stats_sd(self):
        files = [
                os.path.join(pytest.test_dir_samples, 'archive/c/c/baklava.c'),
                os.path.join(pytest.test_dir_samples, 'archive/c/c-plus-plus/bubble-sort.cpp')
        ]
        res, _, _ = self._run(files)

        assert res.get('stats', {}).get('sd', {}).get('loc', 0) == round(statistics.stdev(v.get('loc', 0) for k, v in res.get('files', {}).items()), 3)
        assert res.get('stats', {}).get('sd', {}).get('operands_sum', 0) == round(statistics.stdev(v.get('operands_sum', 0) for k, v in res.get('files', {}).items()), 3)
        assert res.get('stats', {}).get('sd', {}).get('operators_sum', 0) == round(statistics.stdev(v.get('operators_sum', 0) for k, v in res.get('files', {}).items()), 3)
