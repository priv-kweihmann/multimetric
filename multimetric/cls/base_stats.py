class MetricBaseStats():

    def __init__(self, args, **kwargs):
        self._metrics = {}

    def get_results(self, metrics, files="files", overall="overall"):
        """
        This alters the originally passed metrics by calculated ones
        """
        return metrics
