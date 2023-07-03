# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib
class MetricBaseCalc():

    def __init__(self, args, **kwargs):
        self._metrics = {}
        self._internalstore = {}

    def get_results(self, metrics):
        """
        This alters the originally passed metrics by calculated ones
        """
        return metrics

    def get_internal_store(self):
        return self._internalstore
