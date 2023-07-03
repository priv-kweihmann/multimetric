# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib
from multimetric.cls.base import MetricBase
from multimetric.cls.tokentree import TokenTree
from multimetric.cls.tokentree import TokenTreeConfig


class MetricBaseFanout(MetricBase):
    _config = {
        'Go': TokenTreeConfig(
            start=[('Token.Keyword.Namespace', 'import')],
            end=[('Token.Punctuation', r'\)')],
            needle=['Token.Literal.String'],
            trim=['"', "'"]),
        'PHP': TokenTreeConfig(
            start=[('Token.Keyword', 'include'), ('Token.Keyword', 'require'),
                   ('Token.Keyword', 'include_once'), ('Token.Keyword', 'require_once')],
            end=[('Token.Punctuation', ';'), ('Token.Text', '\n')],
            needle=['Token.Literal.String'],
            trim=['"', "'"]),
        'Ruby': TokenTreeConfig(
            start=[('Token.Name.Builtin', 'require')],
            end=[('Token.Text.Whitespace', r'\)')],
            needle=['Token.Literal', 'Token.Literal.String.Double'],
            trim=['"', "'"]),
        'Python': TokenTreeConfig(
            start=[('Token.Keyword.Namespace', 'import'), ('Token.Keyword.Namespace', 'from')],
            end=[('Token.Text', '\n')],
            needle=['Token.Name.Namespace', 'Token.Keyword.Namespace', 'Token.Name'],
            trim=[]),
        'Bash': TokenTreeConfig(
            start=[('Token.Name.Builtin', 'source'), ('Token.Text', r'\.')],
            end=[('Token.Text', '\n'), ('Token.Text', '\n\n')],
            needle=['Token.Text'],
            trim=[' ', '\n']),
        'CoffeeScript': TokenTreeConfig(
            start=[('Token.Name.Other', 'require'), ('Token.Name.Other', 'import')],
            end=[('Token.Text', '\n'), ('Token.Text', '\n\n')],
            needle=['Token.Literal.String'],
            trim=['"', "'", ' ']),
        'C#': TokenTreeConfig(
            start=[('Token.Keyword', 'using')],
            end=[('Token.Punctuation', ';')],
            needle=['Token.Name.Namespace'],
            trim=['"', "'", ' ']),
        'Dart': TokenTreeConfig(
            start=[('Token.Keyword', 'import')],
            end=[('Token.Punctuation', ';')],
            needle=['Token.Literal.String'],
            trim=['"', "'", ' ']),
        'Groovy': TokenTreeConfig(
            start=[('Token.Keyword.Namespace', 'import')],
            end=[('Token.Operator', ';'), ('Token.Text', '\n')],
            needle=['Token.Name.Namespace'],
            trim=[' ']),
        'Haskell': TokenTreeConfig(
            start=[('Token.Keyword.Reserved', 'import')],
            end=[('Token.Text', '\n')],
            needle=['Token.Name.Namespace'],
            trim=[' ']),
        'Julia': TokenTreeConfig(
            start=[('Token.Keyword', 'import'), ('Token.Keyword', 'using')],
            end=[('Token.Text', '\n'), ('Token.Operator', ':')],
            needle=['Token.Name', 'Token.Operator'],
            trim=[' ', ':']),
        'Java': TokenTreeConfig(
            start=[('Token.Keyword.Namespace', 'import')],
            end=[('Token.Text', '\n'), ('Token.Punctuation', ';')],
            needle=['Token.Name.Namespace'],
            trim=[' ']),
        'JavaScript': TokenTreeConfig(
            start=[('Token.Keyword', 'import'), ('Token.Keyword.Reserved', 'from')],
            end=[('Token.Text', '\n'), ('Token.Punctuation', ';'), ('Token.Punctuation', '{')],
            needle=['Token.Literal.String'],
            trim=[' ', '"', "'"]),
        'Kotlin': TokenTreeConfig(
            start=[('Token.Keyword', 'import')],
            end=[('Token.Text', '\n')],
            needle=['Token.Name.Namespace'],
            trim=[' ']),
        'Lua': TokenTreeConfig(
            start=[('Token.Name.Builtin', 'require')],
            end=[('Token.Text', '\n'), ('Token.Text', '\n\n')],
            needle=['Token.Literal.String'],
            trim=[' ', '"', "'"]),
        'Objective-C': TokenTreeConfig(
            start=[('Token.Comment.Preproc', 'import .*')],
            end=[('Token.Comment.Preproc', '\n'), ('Token.Text', '\n'), ('Token.Text', '\n\n')],
            needle=['Token.Comment.Preproc'],
            trim=[' ', '"', "'", '\n', 'import '],
            include_start=True),
        'Prolog': TokenTreeConfig(
            start=[('Token.Literal.String', 'use')],
            end=[('Token.Punctuation', ';'), ('Token.Text', '\n')],
            needle=['Token.Literal'],
            trim=[' ']),
        'Rust': TokenTreeConfig(
            start=[('Token.Keyword', 'use')],
            end=[('Token.Punctuation', ';'), ('Token.Text', '\n')],
            needle=['Token.Name', 'Token.Keyword', 'Token.Literal', 'Token.Text'],
            trim=[' ']),
        'Tcl': TokenTreeConfig(
            start=[('Token.Text', 'import')],
            end=[('Token.Text', 'forget'), ('Token.Text', '\n'), ('Token.Text', '\n\n')],
            needle=['Token.Text'],
            trim=[' ', '-', 'force', 'import', '\n'],
            split_by=' '),
        'TypeScript': TokenTreeConfig(
            start=[('Token.Keyword', 'import'), ('Token.Keyword.Reserved', 'from')],
            end=[('Token.Text', '\n'), ('Token.Punctuation', ';'), ('Token.Punctuation', '{')],
            needle=['Token.Literal.String'],
            trim=[' ', '"', "'"]),
        'Zig': TokenTreeConfig(
            start=[('Token.Name.Builtin', '@import')],
            end=[('Token.Text', '\n'), ('Token.Punctuation', ';')],
            needle=['Token.Literal'],
            trim=[' ', '"', "'"]),
        'default': TokenTreeConfig(
            start=[('Token.Comment.Preproc', 'include'), ('Token.Comment.Namespace', '')],
            end=[('Token.Text.Whitespace', '\n'), ('Token.Comment.Preproc', '\n')],
            needle=['Token.Comment.PreprocFile'],
            trim=[]),
    }

    _internal = {
        "Python": {"start": '.', "end": ''},
        "C": {"start": '"', "end": '"'},
        "C++": {"start": '"', "end": '"'},
        "CoffeeScript": {"start": './', "end": ''},
        "Julia": {"start": '.', "end": ''},
        "TypeScript": {"start": './', "end": ''},
    }

    METRIC_FANOUT_INTERNAL = "fanout_internal"
    METRIC_FANOUT_EXTERNAL = "fanout_external"

    def __init__(self, args, **kwargs):
        super().__init__(args, **kwargs)
        self._int = set()
        self._ext = set()

    def __isInternal(self, value, internal_mapping):
        if not internal_mapping:
            return False
        return all([value.startswith(internal_mapping["start"]),
                    value.endswith(internal_mapping["end"])])

    def parse_tokens(self, language, tokens):
        super().parse_tokens(language, [])

        config = MetricBaseFanout._config.get(language, MetricBaseFanout._config['default'])
        _imports = TokenTree.get_from_token_tree(enumerate(tokens), config)

        for x in _imports:
            if self.__isInternal(x, MetricBaseFanout._internal.get(language, {})):
                self._int.add(str(x))
            else:
                self._ext.add(str(x))
        self._metrics.update({MetricBaseFanout.METRIC_FANOUT_INTERNAL: len(list(self._int)),
                              MetricBaseFanout.METRIC_FANOUT_EXTERNAL: len(list(self._ext))})
        self._internalstore["int"] = list(self._int)
        self._internalstore["ext"] = list(self._ext)

    def get_results_global(self, value_stores):
        _int = []
        _ext = []
        for x in self._get_all_matching_store_objects(value_stores):
            _int += x["int"]
            _ext += x["ext"]
        return {
            MetricBaseFanout.METRIC_FANOUT_INTERNAL: len(_int),
            MetricBaseFanout.METRIC_FANOUT_EXTERNAL: len(_ext),
        }
