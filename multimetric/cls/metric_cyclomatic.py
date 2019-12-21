from multimetric.cls.metric import BaseMetric


class CyclomaticComplexity(BaseMetric):

    __exitPoints = [
        "return",
        "exit"
        "assert",
        "break",
        "continue",
        "yield"
    ]

    __conditions = [
        "if",
        "else",
        "elif",
        "case",
        "default",
        "for",
        "while",
        "and",
        "or",
        "&&",
        "||"
    ]

    def __init__(self, args):
        super().__init__(args)
        self.__conditions = 0
        self.__exitpoints = 0

    def parse_tokens(self, language, tokens):
        super().parse_tokens(language, [])
        for x in tokens:
            if str(x[1]) in CyclomaticComplexity.__exitPoints:
                self.__exitpoints += 1
            if str(x[1]) in CyclomaticComplexity.__conditions:
                self.__conditions += 1

    def get_results(self):
        self._metrics["cyclomatic_complexity"] = max(
            self.__conditions - self.__exitpoints + 2, 0)
        return self._metrics
