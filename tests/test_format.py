# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib
import os

import pytest  # noqa: I900


class TestClassFormat():

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
    
    def __test_format(self, obj, with_lang=True):
        assert 'comment_ratio' in obj
        assert isinstance(obj.get('comment_ratio'), float)

        assert 'cyclomatic_complexity' in obj
        assert isinstance(obj.get('cyclomatic_complexity'), int)

        assert 'fanout_external' in obj
        assert isinstance(obj.get('fanout_external'), int)

        assert 'fanout_internal' in obj
        assert isinstance(obj.get('fanout_internal'), int)

        assert 'halstead_bugprop' in obj
        assert isinstance(obj.get('halstead_bugprop'), float)

        assert 'halstead_difficulty' in obj
        assert isinstance(obj.get('halstead_difficulty'), float)

        assert 'halstead_effort' in obj
        assert isinstance(obj.get('halstead_effort'), float)

        assert 'halstead_timerequired' in obj
        assert isinstance(obj.get('halstead_timerequired'), float)

        assert 'halstead_volume' in obj
        assert isinstance(obj.get('halstead_volume'), float)

        if with_lang:
            assert 'lang' in obj
            assert isinstance(obj.get('lang'), list)
            assert all(isinstance(x, str) for x in obj.get('lang'))
        else:
            assert 'lang' not in obj

        assert 'loc' in obj
        assert isinstance(obj.get('loc'), int)

        assert 'maintainability_index' in obj
        assert isinstance(obj.get('maintainability_index'), int)

        assert 'maintainability_index' in obj
        assert isinstance(obj.get('maintainability_index'), int)

        assert 'maintainability_index' in obj
        assert isinstance(obj.get('maintainability_index'), int)

        assert 'maintainability_index' in obj
        assert isinstance(obj.get('maintainability_index'), int)

        assert 'operands_sum' in obj
        assert isinstance(obj.get('operands_sum'), int)

        assert 'operands_uniq' in obj
        assert isinstance(obj.get('operands_uniq'), int)

        assert 'operators_sum' in obj
        assert isinstance(obj.get('operators_sum'), int)

        assert 'operators_uniq' in obj
        assert isinstance(obj.get('operators_uniq'), int)

        assert 'pylint' in obj
        assert isinstance(obj.get('pylint'), float)

        assert 'tiobe' in obj
        assert isinstance(obj.get('tiobe'), float)

        assert 'tiobe_compiler' in obj
        assert isinstance(obj.get('tiobe_compiler'), float)

        assert 'tiobe_complexity' in obj
        assert isinstance(obj.get('tiobe_complexity'), float)

        assert 'tiobe_coverage' in obj
        assert isinstance(obj.get('tiobe_coverage'), float)

        assert 'tiobe_duplication' in obj
        assert isinstance(obj.get('tiobe_duplication'), float)

        assert 'tiobe_fanout' in obj
        assert isinstance(obj.get('tiobe_fanout'), float)

        assert 'tiobe_functional' in obj
        assert isinstance(obj.get('tiobe_functional'), float)

        assert 'tiobe_functional' in obj
        assert isinstance(obj.get('tiobe_functional'), float)

        assert 'tiobe_security' in obj
        assert isinstance(obj.get('tiobe_security'), float)

        assert 'tiobe_standard' in obj
        assert isinstance(obj.get('tiobe_standard'), float)
    
    def test_format(self):
        file = os.path.join(pytest.test_dir_samples, 'archive/c/c/baklava.c')
        res, _, _ = self._run(file)

        assert isinstance(res, dict)
        assert 'files' in res

        assert isinstance(res.get('files', {}), dict)
        assert file in res.get('files', {})

        self.__test_format(res.get('files', {}).get(file, {}))

    def test_format_overall(self):
        file = os.path.join(pytest.test_dir_samples, 'archive/c/c/baklava.c')
        res, _, _ = self._run(file)

        assert isinstance(res, dict)
        assert 'overall' in res

        self.__test_format(res.get('overall', {}), with_lang=False)

    def test_format_stats_min(self):
        file = os.path.join(pytest.test_dir_samples, 'archive/c/c/baklava.c')
        res, _, _ = self._run(file)

        assert isinstance(res, dict)
        assert 'stats' in res

        assert isinstance(res, dict)
        assert 'min' in res.get('stats', {})

        self.__test_format(res.get('stats', {}).get('min', {}), with_lang=False)

    def test_format_stats_mean(self):
        file = os.path.join(pytest.test_dir_samples, 'archive/c/c/baklava.c')
        res, _, _ = self._run(file)

        assert isinstance(res, dict)
        assert 'stats' in res

        assert isinstance(res, dict)
        assert 'mean' in res.get('stats', {})

        self.__test_format(res.get('stats', {}).get('mean', {}), with_lang=False)

    def test_format_stats_median(self):
        file = os.path.join(pytest.test_dir_samples, 'archive/c/c/baklava.c')
        res, _, _ = self._run(file)

        assert isinstance(res, dict)
        assert 'stats' in res

        assert isinstance(res, dict)
        assert 'median' in res.get('stats', {})

        self.__test_format(res.get('stats', {}).get('median', {}), with_lang=False)

    def test_format_stats_max(self):
        file = os.path.join(pytest.test_dir_samples, 'archive/c/c/baklava.c')
        res, _, _ = self._run(file)

        assert isinstance(res, dict)
        assert 'stats' in res

        assert isinstance(res, dict)
        assert 'max' in res.get('stats', {})

        self.__test_format(res.get('stats', {}).get('max', {}), with_lang=False)
