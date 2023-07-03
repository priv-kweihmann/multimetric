# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib

import os

import pytest  # noqa: I900


class TestClassIntegration():

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
    
    def test_bash(self, file_BASH, capsys):
        result, files, loc = self._run(file_BASH)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'Bash' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_c(self, file_C, capsys):
        result, files, loc = self._run(file_C)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'C' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_cpp(self, file_CPP, capsys):
        result, files, loc = self._run(file_CPP)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'C++' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_coffescript(self, file_COFFEESCRIPT, capsys):
        result, files, loc = self._run(file_COFFEESCRIPT)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'CoffeeScript' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1
    
    def test_csharp(self, file_CSHARP, capsys):
        result, files, loc = self._run(file_CSHARP)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'C#' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_dart(self, file_DART, capsys):
        result, files, loc = self._run(file_DART)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'Dart' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_go(self, file_GO, capsys):
        result, files, loc = self._run(file_GO)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'Go' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_groovy(self, file_GROOVY, capsys):
        result, files, loc = self._run(file_GROOVY)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'Groovy' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_haskell(self, file_HASKELL, capsys):
        result, files, loc = self._run(file_HASKELL)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'Haskell' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_java(self, file_JAVA, capsys):
        result, files, loc = self._run(file_JAVA)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'Java' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1
    
    def test_javascript(self, file_JAVASCRIPT, capsys):
        result, files, loc = self._run(file_JAVASCRIPT)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'JavaScript' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_julia(self, file_JULIA, capsys):
        result, files, loc = self._run(file_JULIA)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'Julia' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_kotlin(self, file_KOTLIN, capsys):
        result, files, loc = self._run(file_KOTLIN)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'Kotlin' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_lisp(self, file_LISP, capsys):
        result, files, loc = self._run(file_LISP)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'NewLisp' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_lua(self, file_LUA, capsys):
        result, files, loc = self._run(file_LUA)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'Lua' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_objectivec(self, file_OBJECTIVEC, capsys):
        result, files, loc = self._run(file_OBJECTIVEC)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'Objective-C' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_perl(self, file_PERL, capsys):
        result, files, loc = self._run(file_PERL)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'Prolog' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_php(self, file_PHP, capsys):
        result, files, loc = self._run(file_PHP)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'PHP' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_python(self, file_PYTHON, capsys):
        result, files, loc = self._run(file_PYTHON)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'Python' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_ruby(self, file_RUBY, capsys):
        result, files, loc = self._run(file_RUBY)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'Ruby' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_rust(self, file_RUST, capsys):
        result, files, loc = self._run(file_RUST)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'Rust' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_tcl(self, file_TCL, capsys):
        result, files, loc = self._run(file_TCL)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'Tcl' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_typescript(self, file_TYPESCRIPT, capsys):
        result, files, loc = self._run(file_TYPESCRIPT)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'TypeScript' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_zig(self, file_ZIG, capsys):
        result, files, loc = self._run(file_ZIG)

        captured = capsys.readouterr()
        assert captured.err == ''
        assert captured.out == ''

        for index, f in enumerate(files):
            assert 'Zig' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1
