# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib
class FilteredImporter():
    def __init__(self, importer, filename):
        self.__importer = importer  # pragma: no cover - bug in pytest-cov
        self.__filefilter = filename  # pragma: no cover - bug in pytest-cov

    def getSumItems(self, _filter=None):
        return self.__importer.getSumItems(_filter={"filename": self.__filefilter, **(_filter or {})})  # pragma: no cover - bug in pytest-cov
