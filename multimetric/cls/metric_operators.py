from multimetric.cls.metric import BaseMetric

# TODO


class OperatorMetric(BaseMetric):
    _needles = [
        "Token.Name.Class",
        "Token.Name.Decorator",
        "Token.Name.Entity",
        "Token.Name.Exception",
        "Token.Name.Function.Magic",
        "Token.Name.Function",
        "Token.Name.Label",
        "Token.Name.Tag",
        "Token.Operator.Word",
        "Token.Operator",
        "Token.Punctuation",
        "Token.String.Affix",
        "Token.String.Delimiter",
    ]

    def __init__(self, args):
        super().__init__(args)
        self.__operator = []

    def parse_tokens(self, language, tokens):
        super().parse_tokens(language, [])
        for x in tokens:
            if str(x[0]) in OperatorMetric._needles:
                self.__operator.append(str(x[1]))

    def get_results(self):
        self._metrics["operators_sum"] = len(self.__operator)
        self._metrics["operators_uniq"] = len(list(set(self.__operator)))
        return self._metrics
