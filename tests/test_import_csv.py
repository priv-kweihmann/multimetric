# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib
import os
import tempfile

import pytest  # noqa: I900


class TestClassCSVImport():

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

    def test_c_plain(self):
        file = os.path.join(pytest.test_dir_local, 'test.c')

        res, _, _ = self._run(file)

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

    def test_c_compiler_warn(self, capsys):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv') as i:
            i.write('test.c,warning,Test warning\n')
            i.flush()

            file = os.path.join(pytest.test_dir_local, 'test.c')

            res, _, _ = self._run(file, '--warn_compiler', i.name)
        
        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        assert res.get('files', {}).get(file, {}).get('pylint', 0) == 99.194
        assert res.get('files', {}).get(file, {}).get('tiobe', 0) == 89.017
        assert res.get('files', {}).get(file, {}).get('tiobe_compiler', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_complexity', 0) == 26.778
        assert res.get('files', {}).get(file, {}).get('tiobe_coverage', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_duplication', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_fanout', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_functional', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_security', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_standard', 0) == 100.0

    def test_c_functional_warn(self, capsys):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv') as i:
            i.write('test.c,warning,Test warning\n')
            i.flush()

            file = os.path.join(pytest.test_dir_local, 'test.c')

            res, _, _ = self._run(file, '--warn_functional', i.name)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        assert res.get('files', {}).get(file, {}).get('pylint', 0) == 99.194
        assert res.get('files', {}).get(file, {}).get('tiobe', 0) == 89.017
        assert res.get('files', {}).get(file, {}).get('tiobe_compiler', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_complexity', 0) == 26.778
        assert res.get('files', {}).get(file, {}).get('tiobe_coverage', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_duplication', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_fanout', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_functional', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_security', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_standard', 0) == 100.0

    def test_c_security_warn(self, capsys):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv') as i:
            i.write('test.c,warning,Test warning\n')
            i.flush()

            file = os.path.join(pytest.test_dir_local, 'test.c')

            res, _, _ = self._run(file, '--warn_security', i.name)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        assert res.get('files', {}).get(file, {}).get('pylint', 0) == 99.194
        assert res.get('files', {}).get(file, {}).get('tiobe', 0) == 89.017
        assert res.get('files', {}).get(file, {}).get('tiobe_compiler', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_complexity', 0) == 26.778
        assert res.get('files', {}).get(file, {}).get('tiobe_coverage', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_duplication', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_fanout', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_functional', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_security', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_standard', 0) == 100.0

    def test_c_compiler_error(self, capsys):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv') as i:
            i.write('test.c,error,Test warning\n')
            i.flush()

            file = os.path.join(pytest.test_dir_local, 'test.c')

            res, _, _ = self._run(file, '--warn_compiler', i.name)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        assert res.get('files', {}).get(file, {}).get('pylint', 0) == 95.968
        assert res.get('files', {}).get(file, {}).get('tiobe', 0) == 89.017
        assert res.get('files', {}).get(file, {}).get('tiobe_compiler', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_complexity', 0) == 26.778
        assert res.get('files', {}).get(file, {}).get('tiobe_coverage', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_duplication', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_fanout', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_functional', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_security', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_standard', 0) == 100.0

    def test_c_functional_error(self, capsys):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv') as i:
            i.write('test.c,error,Test warning\n')
            i.flush()

            file = os.path.join(pytest.test_dir_local, 'test.c')

            res, _, _ = self._run(file, '--warn_functional', i.name)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        assert res.get('files', {}).get(file, {}).get('pylint', 0) == 95.968
        assert res.get('files', {}).get(file, {}).get('tiobe', 0) == 89.017
        assert res.get('files', {}).get(file, {}).get('tiobe_compiler', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_complexity', 0) == 26.778
        assert res.get('files', {}).get(file, {}).get('tiobe_coverage', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_duplication', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_fanout', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_functional', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_security', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_standard', 0) == 100.0

    def test_c_security_error(self, capsys):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv') as i:
            i.write('test.c,error,Test warning\n')
            i.flush()

            file = os.path.join(pytest.test_dir_local, 'test.c')

            res, _, _ = self._run(file, '--warn_security', i.name)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        assert res.get('files', {}).get(file, {}).get('pylint', 0) == 95.968
        assert res.get('files', {}).get(file, {}).get('tiobe', 0) == 89.017
        assert res.get('files', {}).get(file, {}).get('tiobe_compiler', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_complexity', 0) == 26.778
        assert res.get('files', {}).get(file, {}).get('tiobe_coverage', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_duplication', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_fanout', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_functional', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_security', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_standard', 0) == 100.0

    def test_c_compiler_info(self, capsys):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv') as i:
            i.write('test.c,info,Test warning\n')
            i.flush()

            file = os.path.join(pytest.test_dir_local, 'test.c')

            res, _, _ = self._run(file, '--warn_compiler', i.name)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        assert 'C' in res.get('files', {}).get(file, {}).get('lang', [])
        assert res.get('files', {}).get(file, {}).get('pylint', 0) == 99.194
        assert res.get('files', {}).get(file, {}).get('tiobe', 0) == 89.017
        assert res.get('files', {}).get(file, {}).get('tiobe_compiler', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_complexity', 0) == 26.778
        assert res.get('files', {}).get(file, {}).get('tiobe_coverage', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_duplication', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_fanout', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_functional', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_security', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_standard', 0) == 100.0

    def test_c_functional_info(self, capsys):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv') as i:
            i.write('test.c,info,Test warning\n')
            i.flush()

            file = os.path.join(pytest.test_dir_local, 'test.c')

            res, _, _ = self._run(file, '--warn_functional', i.name)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        assert 'C' in res.get('files', {}).get(file, {}).get('lang', [])
        assert res.get('files', {}).get(file, {}).get('pylint', 0) == 99.194
        assert res.get('files', {}).get(file, {}).get('tiobe', 0) == 89.017
        assert res.get('files', {}).get(file, {}).get('tiobe_compiler', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_complexity', 0) == 26.778
        assert res.get('files', {}).get(file, {}).get('tiobe_coverage', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_duplication', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_fanout', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_functional', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_security', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_standard', 0) == 100.0

    def test_c_security_info(self, capsys):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv') as i:
            i.write('test.c,info,Test warning\n')
            i.flush()

            file = os.path.join(pytest.test_dir_local, 'test.c')

            res, _, _ = self._run(file, '--warn_security', i.name)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        assert 'C' in res.get('files', {}).get(file, {}).get('lang', [])
        assert res.get('files', {}).get(file, {}).get('pylint', 0) == 99.194
        assert res.get('files', {}).get(file, {}).get('tiobe', 0) == 89.017
        assert res.get('files', {}).get(file, {}).get('tiobe_compiler', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_complexity', 0) == 26.778
        assert res.get('files', {}).get(file, {}).get('tiobe_coverage', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_duplication', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_fanout', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_functional', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_security', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_standard', 0) == 100.0

    def test_c_security_warning_content_number(self, capsys):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv') as i:
            i.write('test.c,warning,123\n')
            i.flush()

            file = os.path.join(pytest.test_dir_local, 'test.c')

            res, _, _ = self._run(file, '--warn_security', i.name)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        assert 'C' in res.get('files', {}).get(file, {}).get('lang', [])
        assert res.get('files', {}).get(file, {}).get('pylint', 0) == 0.806
        assert res.get('files', {}).get(file, {}).get('tiobe', 0) == 89.017
        assert res.get('files', {}).get(file, {}).get('tiobe_compiler', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_complexity', 0) == 26.778
        assert res.get('files', {}).get(file, {}).get('tiobe_coverage', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_duplication', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_fanout', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_functional', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_security', 0) == 100.0
        assert res.get('files', {}).get(file, {}).get('tiobe_standard', 0) == 100.0
