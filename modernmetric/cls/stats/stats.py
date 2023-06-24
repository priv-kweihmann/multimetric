import statistics

from modernmetric.cls.base_stats import MetricBaseStats


class MetricBaseStatsAverage(MetricBaseStats):

    def __init__(self, args, **kwargs):
        super().__init__(args, **kwargs)

    def _getInputList(self, metrics, key):
        res = []
        for _, v in metrics.items():
            if key in v and not isinstance(v[key], list):
                res.append(v[key])
        return res

    def get_results(self, metrics, files="files", overall="overall"):
        _keylist = list(metrics[overall].keys())
        metrics["stats"] = {}
        metrics["stats"]["mean"] = {}
        metrics["stats"]["max"] = {}
        metrics["stats"]["min"] = {}
        if len(metrics["files"]) > 1:
            metrics["stats"]["sd"] = {}
        metrics["stats"]["median"] = {}
        for k in _keylist:
            _list = self._getInputList(metrics[files], k)
            if not _list:
                continue
            metrics["stats"]["mean"][k] = statistics.mean(_list)
            metrics["stats"]["median"][k] = statistics.median(_list)
            metrics["stats"]["max"][k] = max(_list)
            metrics["stats"]["min"][k] = min(_list)
            if len(metrics["files"]) > 1:
                metrics["stats"]["sd"][k] = statistics.stdev(_list)
        return super().get_results(metrics, files="files", overall="overall")
