from multimetric.cls.base import MetricBase


class MetricBaseOperator(MetricBase):
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

    METRIC_OPERATORS_SUM = "operators_sum"
    METRIC_OPERATORS_UNIQUE = "operators_uniq"

    def __init__(self, args):
        super().__init__(args)
        self.__operator = []

    def parse_tokens(self, language, tokens):
        super().parse_tokens(language, [])
        for x in tokens:
            if str(x[0]) in MetricBaseOperator._needles:
                self.__operator.append(str(x[1]))

    def get_results(self):
        self._metrics[MetricBaseOperator.METRIC_OPERATORS_SUM] = len(self.__operator)
        self._metrics[MetricBaseOperator.METRIC_OPERATORS_UNIQUE] = len(list(set(self.__operator)))
        return self._metrics
