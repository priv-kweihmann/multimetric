from multimetric.cls.base import MetricBase


class MetricBaseFanout(MetricBase):
    _needles = {
        "Python": [
            "Token.Name.Namespace",
        ],
        "C": [
            "Token.Comment.PreprocFile",
        ],
        "C++": [
            "Token.Comment.PreprocFile",
        ],
    }
    _functions = {
        "PHP": "_parsePHP",
        "Go": "_parseGo",
        "Ruby": "_parseRuby",
    }
    _internal = {
        "Python": {"start": ".", "end": ""},
        "C": {"start": "\"", "end": "\""},
        "C++": {"start": "\"", "end": "\""},
    }

    METRIC_FANOUT_INTERNAL = "fanout_internal"
    METRIC_FANOUT_EXTERNAL = "fanout_external"

    def __init__(self, args, **kwargs):
        super().__init__(args, **kwargs)
        self._int = set()
        self._ext = set()

    def __isInternal(self, value, internal_mapping):
        return all([value.startswith(internal_mapping["start"]),
                    value.endswith(internal_mapping["end"])])

    def _parsePHP(self, iterator):
        res = []
        _start_token = ["include", "require", "include_once", "require_once"]
        _cont_token = ["Token.Literal.String.Single", "Token.Literal.String.Double"]
        for _, value in iterator:
            if str(value[0]) in ["Token.Keyword"] and value[1] in _start_token:
                while iterator and str(value[0]) not in _cont_token:
                    try:
                        _, value = next(iterator)
                    except StopIteration:
                        break
                if iterator:
                    res.append(value[1].strip("'").strip('"'))
        return res

    def _parseRuby(self, iterator):
        res = []
        for i, value in iterator:
            if str(value[0]) in ["Token.Name.Builtin"] and value[1] in ["require"]:
                while iterator:
                    i, value = next(iterator)
                    if str(value[0]) in ["Token.Literal.String.Single"]:
                        res.append(value[1].strip("'").strip('"'))
                        break
                    elif str(value[0]) in ["Token.Text"] and value[1] in ["\n", "\r\n"]:
                        break
        return res

    def _parseGo(self, iterator):
        res = []
        for _, value in iterator:
            if str(value[0]) in ["Token.Keyword.Namespace"] and value[1] in ["import"]:
                while iterator:
                    try:
                        _, value = next(iterator)
                        if str(value[0]) in ["Token.Literal.String"]:
                            res.append(value[1].strip("'").strip('"'))
                        if str(value[0]) in ["Token.Punctuation"] and value[1] in [')']:
                            break
                    except StopIteration:
                        break
        return res

    def parse_tokens(self, language, tokens):
        super().parse_tokens(language, [])
        if language in MetricBaseFanout._internal:
            _i = MetricBaseFanout._internal[language]
        else:
            _i = {"start": "", "end": ""}
        _imports = []
        if language in MetricBaseFanout._needles.keys():
            _n = MetricBaseFanout._needles[language]
            for x in [x for x in tokens if str(x[0]) in _n]:
                _imports.append(x[1])
        elif language in MetricBaseFanout._functions:
            _imports = getattr(self,
                               MetricBaseFanout._functions[language])(enumerate(tokens))
        for x in _imports:
            if self.__isInternal(x, _i):
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
