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
        return (run(args_), file)
    
    def test_bash(self, file_BASH):
        result, files = self._run(file_BASH)

        for f in files:
            assert 'Bash' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0

    def test_c(self, file_C):
        result, files = self._run(file_C)

        for f in files:
            assert 'C' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0

    def test_cpp(self, file_CPP):
        result, files = self._run(file_CPP)

        for f in files:
            assert 'C++' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0

    def test_coffescript(self, file_COFFEESCRIPT):
        result, files = self._run(file_COFFEESCRIPT)

        for f in files:
            assert 'CoffeeScript' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
    
    def test_csharp(self, file_CSHARP):
        result, files = self._run(file_CSHARP)

        for f in files:
            assert 'C#' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0

    def test_dart(self, file_DART):
        result, files = self._run(file_DART)

        for f in files:
            assert 'Dart' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0

    def test_groovy(self, file_GROOVY):
        result, files = self._run(file_GROOVY)

        for f in files:
            assert 'Groovy' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0

    def test_haskell(self, file_HASKELL):
        result, files = self._run(file_HASKELL)

        for f in files:
            assert 'Haskell' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0

    def test_java(self, file_JAVA):
        result, files = self._run(file_JAVA)

        for f in files:
            assert 'Java' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0
    
    def test_javascript(self, file_JAVASCRIPT):
        result, files = self._run(file_JAVASCRIPT)

        for f in files:
            assert 'JavaScript' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0

    def test_julia(self, file_JULIA):
        result, files = self._run(file_JULIA)

        for f in files:
            assert 'Julia' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0

    def test_kotlin(self, file_KOTLIN):
        result, files = self._run(file_KOTLIN)

        for f in files:
            assert 'Kotlin' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0

    def test_lisp(self, file_LISP):
        result, files = self._run(file_LISP)

        for f in files:
            assert 'NewLisp' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0

    def test_lua(self, file_LUA):
        result, files = self._run(file_LUA)

        for f in files:
            assert 'Lua' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0

    def test_objectivec(self, file_OBJECTIVEC):
        result, files = self._run(file_OBJECTIVEC)

        for f in files:
            assert 'Objective-C' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0

    def test_perl(self, file_PERL):
        result, files = self._run(file_PERL)

        for f in files:
            assert 'Prolog' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0

    def test_php(self, file_PHP):
        result, files = self._run(file_PHP)

        for f in files:
            assert 'PHP' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0

    def test_python(self, file_PYTHON):
        result, files = self._run(file_PYTHON)

        for f in files:
            assert 'Python' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0

    def test_ruby(self, file_RUBY):
        result, files = self._run(file_RUBY)

        for f in files:
            assert 'Ruby' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0

    def test_rust(self, file_RUST):
        result, files = self._run(file_RUST)

        for f in files:
            assert 'Rust' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0

    def test_tcl(self, file_TCL):
        result, files = self._run(file_TCL)

        for f in files:
            assert 'Tcl' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0

    def test_typescript(self, file_TYPESCRIPT):
        result, files = self._run(file_TYPESCRIPT)

        for f in files:
            assert 'TypeScript' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0

    def test_zig(self, file_ZIG):
        result, files = self._run(file_ZIG)

        for f in files:
            assert 'Zig' in result.get('files', {}).get(f, {}).get('lang', [])
            assert result.get('files', {}).get(f, {}).get('operands_sum', 0) > 0