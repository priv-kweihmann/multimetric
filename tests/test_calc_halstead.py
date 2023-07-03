# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib
import os

import pytest  # noqa: I900


class TestClassHalstead():

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
    
    def test_halstead_default(self):
        file = os.path.join(pytest.test_dir_local, 'test.c')

        res, _, _ = self._run(file)

        assert res.get('files', {}).get(file, {}).get('halstead_bugprop', 0) == 0.207
        assert res.get('files', {}).get(file, {}).get('halstead_difficulty', 0) == 23.233
        assert res.get('files', {}).get(file, {}).get('halstead_effort', 0) == 14404.667
        assert res.get('files', {}).get(file, {}).get('halstead_timerequired', 0) == 800.259
        assert res.get('files', {}).get(file, {}).get('halstead_volume', 0) == 620.0

    def test_halstead_old(self):
        file = os.path.join(pytest.test_dir_local, 'test.c')

        res, _, _ = self._run(file, '--bugpredict', 'old')

        assert res.get('files', {}).get(file, {}).get('halstead_bugprop', 0) == 3.201
        assert res.get('files', {}).get(file, {}).get('halstead_difficulty', 0) == 23.233
        assert res.get('files', {}).get(file, {}).get('halstead_effort', 0) == 14404.667
        assert res.get('files', {}).get(file, {}).get('halstead_timerequired', 0) == 800.259
        assert res.get('files', {}).get(file, {}).get('halstead_volume', 0) == 620.0

    def test_halstead_new(self):
        file = os.path.join(pytest.test_dir_local, 'test.c')

        res, _, _ = self._run(file, '--bugpredict', 'new')

        assert res.get('files', {}).get(file, {}).get('halstead_bugprop', 0) == 0.207
        assert res.get('files', {}).get(file, {}).get('halstead_difficulty', 0) == 23.233
        assert res.get('files', {}).get(file, {}).get('halstead_effort', 0) == 14404.667
        assert res.get('files', {}).get(file, {}).get('halstead_timerequired', 0) == 800.259
        assert res.get('files', {}).get(file, {}).get('halstead_volume', 0) == 620.0

