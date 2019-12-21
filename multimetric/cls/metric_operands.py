from multimetric.cls.metric import BaseMetric


class OperandsMetric(BaseMetric):
    _needles = [
        "Token.Literal.Date",
        "Token.Literal.String.Double",
        "Token.Literal.String",
        "Token.Literal.Number.Bin",
        "Token.Literal.Number.Float",
        "Token.Literal.Number.Hex",
        "Token.Literal.Number.Integer.Long",
        "Token.Literal.Number.Integer",
        "Token.Literal.Number.Oct",
        "Token.Literal.Number",
        "Token.Name",
        "Token.Name.Attribute",
        "Token.Name.Builtin.Pseudo",
        "Token.Name.Builtin",
        "Token.Name.Constant",
        "Token.Name.Variable.Class",
        "Token.Name.Variable.Global",
        "Token.Name.Variable.Instance",
        "Token.Name.Variable.Magic",
        "Token.Name.Variable",
        "Token.Name.Other",
        "Token.Number.Bin",
        "Token.Number.Float",
        "Token.Number.Hex",
        "Token.Number.Integer.Long",
        "Token.Number.Integer",
        "Token.Number.Oct",
        "Token.Number",
        "Token.String.Char",
        "Token.String.Double",
        "Token.String.Escape",
        "Token.String.Heredoc",
        "Token.String.Interpol",
        "Token.String.Other",
        "Token.String.Regex",
        "Token.String.Single",
        "Token.String.Symbol"
    ]

    def __init__(self, args):
        super().__init__(args)
        self.__operands = []

    def parse_tokens(self, language, tokens):
        super().parse_tokens(language, [])
        for x in tokens:
            if str(x[0]) in OperandsMetric._needles:
                self.__operands.append(str(x[1]))

    def get_results(self):
        self._metrics["operands_sum"] = len(self.__operands)
        self._metrics["operands_uniq"] = len(list(set(self.__operands)))
        return self._metrics
