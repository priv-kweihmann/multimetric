class MetricBase():
    def __init__(self, args, **kwargs):
        self._metrics = {"lang": []}
        self._internalstore = {}

    def parse_tokens(self, language, tokens):
        if language not in self._metrics["lang"]:
            self._metrics["lang"].append(language)

    def get_results(self):
        return self._metrics

    def get_internal_store(self):
        return {self.__class__.__name__: self._internalstore}

    def _get_all_matching_store_objects(self, store):
        res = []
        for item in store:
            if self.__class__.__name__ in item:
                res.append(item[self.__class__.__name__])
        return res

    def get_results_global(self, value_stores):
        return {}  # pragma: no cover
