from multimetric.cls.metric import BaseMetric


class Fanout(BaseMetric):
    _needles = {
        "Python": [
            "Token.Name.Namespace"
        ],
        "C": [
            "Token.Comment.PreprocFile"
        ],
        "C++": [
            "Token.Comment.PreprocFile"
        ]
    }
    _functions = {
        "PHP": "_parsePHP",
        "Go": "_parseGo"
    }
    _internal = {
        "Python": {"start": ".", "end": ""},
        "C": {"start": "\"", "end": "\""},
        "C++": {"start": "\"", "end": "\""}
    }

    def __init__(self, args):
        super().__init__(args)
        self._int = set()
        self._ext = set()

    def __isInternal(self, value, internal_mapping):
        return all([value.startswith(internal_mapping["start"]),
                   value.endswith(internal_mapping["end"])])

    def _parsePHP(self, iterator):
        res = []
        for i, val in iterator:
            if str(val[0]) in ["Token.Keyword"] and val[1] in ["include", "require", "include_once", "require_once"]:
                while iterator and str(val[0]) not in ["Token.Literal.String.Single", "Token.Literal.String.Double"]:
                    i, val = next(iterator)
                if iterator:
                    res.append(val[1].strip("'").strip('"'))
        return res

    def _parseGo(self, iterator):
        res = []
        for i, val in iterator:
            if str(val[0]) in ["Token.Keyword.Namespace"] and val[1] in ["import"]:
                while iterator:
                    i, val = next(iterator)
                    if str(val[0]) in ["Token.Literal.String"]:
                        res.append(val[1].strip("'").strip('"'))
                    if str(val[0]) in ["Token.Punctuation"] and val[1] in [')']:
                        break
        return res

    def parse_tokens(self, language, tokens):
        super().parse_tokens(language, [])
        if language in Fanout._internal:
            _i = Fanout._internal[language]
        else:
            _i = {"start": "", "end": ""}
        _imports = []
        if language in Fanout._needles.keys():
            _n = Fanout._needles[language]
            for x in [x for x in tokens if str(x[0]) in _n]:
                _imports.append(x[1])
        elif language in Fanout._functions:
            _imports = getattr(self,
                               Fanout._functions[language])(enumerate(tokens))
        # else:
        #     # Language isn't supported at the moment
        #     for x in tokens:
        #         print(str(x))
        for x in _imports:
            if self.__isInternal(x, _i):
                self._int.add(str(x))
            else:
                self._ext.add(str(x))
        self._metrics.update({"fanout_internal": len(list(self._int)),
                              "fanout_external": len(list(self._ext))})
