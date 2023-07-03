# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib
from multimetric.cls.base import MetricBase


class MetricBaseOperands(MetricBase):
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
        "Token.String.Symbol",
    ]

    METRIC_OPERANDS_SUM = "operands_sum"
    METRIC_OPERANDS_UNIQUE = "operands_uniq"

    def __init__(self, args, **kwargs):
        super().__init__(args, **kwargs)
        self.__operands = []

    def parse_tokens(self, language, tokens):
        super().parse_tokens(language, [])
        for x in tokens:
            if str(x[0]) in MetricBaseOperands._needles:
                self.__operands.append(str(x[1]))

    def get_results(self):
        self._metrics[MetricBaseOperands.METRIC_OPERANDS_SUM] = len(self.__operands)
        self._metrics[MetricBaseOperands.METRIC_OPERANDS_UNIQUE] = len(list(set(self.__operands)))

        self._internalstore["operands"] = self.__operands
        return self._metrics

    def get_results_global(self, value_stores):
        _operands = []
        for x in self._get_all_matching_store_objects(value_stores):
            _operands += x["operands"]
        return {
            MetricBaseOperands.METRIC_OPERANDS_SUM: len(_operands),
            MetricBaseOperands.METRIC_OPERANDS_UNIQUE: len(list(set(_operands))),
        }
