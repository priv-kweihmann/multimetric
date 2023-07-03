# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib
import os
import tempfile
import json

import pytest  # noqa: I900


class TestClassImportCornerCases():

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

    def test_c_compiler_warn_corrupt_csv(self, capsys):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv') as i:
            i.write('test.c,\n')
            i.flush()

            file = os.path.join(pytest.test_dir_local, 'test.c')

            res, _, _ = self._run(file, '--warn_compiler', i.name)

        captured = capsys.readouterr()
        assert any(captured.err)
        assert captured.out == ''

        assert res.get('files', {}).get(file, {}).get('pylint', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe', 0) == 89.017
        assert res.get('files', {}).get(file, {}).get('tiobe_compiler', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_complexity', 0) == 26.778
        assert res.get('files', {}).get(file, {}).get('tiobe_coverage', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_duplication', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_fanout', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_functional', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_security', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_standard', 0) == 100.0

    def test_c_compiler_warn_corrupt_json(self, capsys):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json') as i:
            i.write("{'test.c': {'severity': 'warning', 'content': 'Test warning'}")
            i.flush()

            file = os.path.join(pytest.test_dir_local, 'test.c')

            res, _, _ = self._run(file, '--warn_compiler', i.name)
        
        captured = capsys.readouterr()
        assert any(captured.err)
        assert captured.out == ''

        assert res.get('files', {}).get(file, {}).get('pylint', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe', 0) == 89.017
        assert res.get('files', {}).get(file, {}).get('tiobe_compiler', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_complexity', 0) == 26.778
        assert res.get('files', {}).get(file, {}).get('tiobe_coverage', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_duplication', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_fanout', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_functional', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_security', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_standard', 0) == 100.0
    
    def test_c_compiler_warn_unsupported_ext(self, capsys):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.ext') as i:
            i.write('test.c,info,123\n')
            i.flush()

            file = os.path.join(pytest.test_dir_local, 'test.c')

            res, _, _ = self._run(file, '--warn_compiler', i.name)
        
        captured = capsys.readouterr()
        assert any(captured.err)
        assert captured.out == ''

        assert res.get('files', {}).get(file, {}).get('pylint', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe', 0) == 89.017
        assert res.get('files', {}).get(file, {}).get('tiobe_compiler', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_complexity', 0) == 26.778
        assert res.get('files', {}).get(file, {}).get('tiobe_coverage', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_duplication', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_fanout', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_functional', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_security', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_standard', 0) == 100.0