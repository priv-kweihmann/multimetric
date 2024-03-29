# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib
import csv
import logging

from multimetric.cls.importer.base import Importer


class ImporterCSV(Importer):

    def __init__(self, args, filearg):
        super().__init__(args, filearg)
        self.__readInput()

    def __readInput(self):
        try:
            with open(self._input) as i:
                reader = csv.reader(i)
                for row in reader:
                    self._items.append(Importer.ImporterItem.from_csv(row))
        except Exception as e:
            logging.getLogger('stderr').error(f"Read error: {e}\n")
