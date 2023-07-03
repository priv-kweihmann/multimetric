# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib
import os
import tempfile
import json

import pytest  # noqa: I900


class TestClassCornerCases():

    def _run(self, in_, *args):
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

    def test_unknown_filetype(self, capsys):

        file = os.path.join(pytest.test_dir_local, 'unknown.test')

        res, _, _ = self._run(file)

        captured = capsys.readouterr()
        #assert any(captured.err)
        assert captured.out == ''

        assert res.get('files', {}).get(file, {}).get('comment_ratio', 0) == 0
        assert res.get('files', {}).get(file, {}).get('cyclomatic_complexity', 0) == 0
        assert res.get('files', {}).get(file, {}).get('fanout_external', 0) == 0
        assert res.get('files', {}).get(file, {}).get('fanout_internal', 0) == 0
        assert res.get('files', {}).get(file, {}).get('loc', 0) == 0
        assert res.get('files', {}).get(file, {}).get('operands_sum', 0) == 0
        assert res.get('files', {}).get(file, {}).get('operands_uniq', 0) == 0
        assert res.get('files', {}).get(file, {}).get('operators_sum', 0) == 0
        assert res.get('files', {}).get(file, {}).get('operators_uniq', 0) == 0

    def test_empty_file(self, capsys):

        file = os.path.join(pytest.test_dir_local, 'empty.c')

        res, _, _ = self._run(file)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        assert res.get('files', {}).get(file, {}).get('comment_ratio', 0) == 0
        assert res.get('files', {}).get(file, {}).get('cyclomatic_complexity', 0) == 0
        assert res.get('files', {}).get(file, {}).get('fanout_external', 0) == 0
        assert res.get('files', {}).get(file, {}).get('fanout_internal', 0) == 0
        assert res.get('files', {}).get(file, {}).get('loc', 0) == 0
        assert res.get('files', {}).get(file, {}).get('operands_sum', 0) == 0
        assert res.get('files', {}).get(file, {}).get('operands_uniq', 0) == 0
        assert res.get('files', {}).get(file, {}).get('operators_sum', 0) == 0
        assert res.get('files', {}).get(file, {}).get('operators_uniq', 0) == 0
