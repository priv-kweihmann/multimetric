# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib
class FilteredImporter():
    def __init__(self, importer, filename):
        self.__importer = importer
        self.__filefilter = filename

    def getSumItems(self, _filter=None):
        return self.__importer.getSumItems(_filter={"filename": self.__filefilter, **(_filter or {})})
