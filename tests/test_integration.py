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
    
    def test_bash(self, file_BASH):
        result, files, loc = self._run(file_BASH)

        for index, f in enumerate(files):
            assert 'Bash' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_c(self, file_C):
        result, files, loc = self._run(file_C)

        for index, f in enumerate(files):
            assert 'C' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_cpp(self, file_CPP):
        result, files, loc = self._run(file_CPP)

        for index, f in enumerate(files):
            assert 'C++' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_coffescript(self, file_COFFEESCRIPT):
        result, files, loc = self._run(file_COFFEESCRIPT)

        for index, f in enumerate(files):
            assert 'CoffeeScript' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1
    
    def test_csharp(self, file_CSHARP):
        result, files, loc = self._run(file_CSHARP)

        for index, f in enumerate(files):
            assert 'C#' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_dart(self, file_DART):
        result, files, loc = self._run(file_DART)

        for index, f in enumerate(files):
            assert 'Dart' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_go(self, file_GO):
        result, files, loc = self._run(file_GO)

        for index, f in enumerate(files):
            assert 'Go' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_groovy(self, file_GROOVY):
        result, files, loc = self._run(file_GROOVY)

        for index, f in enumerate(files):
            assert 'Groovy' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_haskell(self, file_HASKELL):
        result, files, loc = self._run(file_HASKELL)

        for index, f in enumerate(files):
            assert 'Haskell' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_java(self, file_JAVA):
        result, files, loc = self._run(file_JAVA)

        for index, f in enumerate(files):
            assert 'Java' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1
    
    def test_javascript(self, file_JAVASCRIPT):
        result, files, loc = self._run(file_JAVASCRIPT)

        for index, f in enumerate(files):
            assert 'JavaScript' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_julia(self, file_JULIA):
        result, files, loc = self._run(file_JULIA)

        for index, f in enumerate(files):
            assert 'Julia' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_kotlin(self, file_KOTLIN):
        result, files, loc = self._run(file_KOTLIN)

        for index, f in enumerate(files):
            assert 'Kotlin' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_lisp(self, file_LISP):
        result, files, loc = self._run(file_LISP)

        for index, f in enumerate(files):
            assert 'NewLisp' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_lua(self, file_LUA):
        result, files, loc = self._run(file_LUA)

        for index, f in enumerate(files):
            assert 'Lua' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_objectivec(self, file_OBJECTIVEC):
        result, files, loc = self._run(file_OBJECTIVEC)

        for index, f in enumerate(files):
            assert 'Objective-C' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_perl(self, file_PERL):
        result, files, loc = self._run(file_PERL)

        for index, f in enumerate(files):
            assert 'Prolog' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_php(self, file_PHP):
        result, files, loc = self._run(file_PHP)

        for index, f in enumerate(files):
            assert 'PHP' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_python(self, file_PYTHON):
        result, files, loc = self._run(file_PYTHON)

        for index, f in enumerate(files):
            assert 'Python' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_ruby(self, file_RUBY):
        result, files, loc = self._run(file_RUBY)

        for index, f in enumerate(files):
            assert 'Ruby' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_rust(self, file_RUST):
        result, files, loc = self._run(file_RUST)

        for index, f in enumerate(files):
            assert 'Rust' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_tcl(self, file_TCL):
        result, files, loc = self._run(file_TCL)

        for index, f in enumerate(files):
            assert 'Tcl' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_typescript(self, file_TYPESCRIPT):
        result, files, loc = self._run(file_TYPESCRIPT)

        for index, f in enumerate(files):
            assert 'TypeScript' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1

    def test_zig(self, file_ZIG):
        result, files, loc = self._run(file_ZIG)

        for index, f in enumerate(files):
            assert 'Zig' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
            if loc[index] > 1:
                assert result.get('files', {}).get(f, {}).get('loc', 0) > 1
