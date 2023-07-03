# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib
class Importer():

    class ImporterItem():

        def __init__(self, _file, _cnt, _sev):
            self._values = {
                "filename": _file,
                "content": _cnt,
                "severity": _sev,
            }

        def match(self, _filter):
            res = _filter.get('filename', '').endswith(self._values['filename'])
            res &= _filter.get('severity', '') == self._values.get('severity', '')
            return res

        def get(self):
            return self._values  # pragma: no cover - bug in pytest-cov

        @staticmethod
        def from_csv(line):
            _cnt = ''
            if len(line) > 2:
                _cnt = line[2]
            if not line[0] or not line[1]:
                raise Exception('Broken CSV')
            return Importer.ImporterItem(_file=line[0], _sev=line[1], _cnt=_cnt)

    def __init__(self, args, filearg):
        self._input = filearg
        self._items = []

    def getItems(self, _filter=None):
        return [x.get() for x in self._items if x.match(_filter or {})]

    def getSumItems(self, _filter=None):
        _items = self.getItems(_filter=_filter)
        if len(_items) == 1:
            if str.isdigit(_items[0]["content"]):  # pragma: no cover - bug in pytest-cov
                return int(_items[0]["content"])  # pragma: no cover - bug in pytest-cov
        return len(_items)
