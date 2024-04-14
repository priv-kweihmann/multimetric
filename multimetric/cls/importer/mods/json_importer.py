# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib
import json
import logging

from multimetric.cls.importer.base import Importer


class ImporterJSON(Importer):

    def __init__(self, args, filearg):
        super().__init__(args, filearg)
        self.__readInput()

    def __readInput(self):
        try:
            with open(self._input) as i:
                reader = json.load(i)
                for k, v in reader.items():
                    self._items.append(Importer.ImporterItem(_file=k,
                                                             _sev=v["severity"],
                                                             _cnt=v.get('content', None)))
        except Exception as e:
            logging.getLogger('stderr').error(f"Read error: {e}\n")
