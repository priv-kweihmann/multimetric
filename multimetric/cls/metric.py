class BaseMetric():
    def __init__(self, args):
        self._metrics = {"lang": []}

    def parse_tokens(self, language, tokens):
        if language not in self._metrics["lang"]:
            self._metrics["lang"].append(language)

    def get_results(self):
        return self._metrics


class CalcMetric():

    def __init__(self, args):
        self._metrics = {}

    def get_results(self, metrics):
        """
        This alters the originally passed metrics by calculated ones
        """
        return metrics


class AverageMetric():

    def __init__(self, args):
        self._metrics = {}

    def get_results(self, metrics, files="files", overall="overall"):
        """
        This alters the originally passed metrics by calculated ones
        """
        return metrics
