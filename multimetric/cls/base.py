class MetricBase():
    def __init__(self, args, **kwargs):
        self._metrics = {"lang": []}

    def parse_tokens(self, language, tokens):
        if language not in self._metrics["lang"]:
            self._metrics["lang"].append(language)

    def get_results(self):
        return self._metrics
