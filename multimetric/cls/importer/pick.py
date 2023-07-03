# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib
import os
import logging

from multimetric.cls.importer.base import Importer
from multimetric.cls.importer.mods.csv import ImporterCSV
from multimetric.cls.importer.mods.json import ImporterJSON


def importer_pick(args, filearg):  # noqa: CFQ004
    if not filearg:
        return None
    _file, _ext = os.path.splitext(filearg)
    if _ext in [".csv"]:
        return ImporterCSV(args, filearg)
    if _ext in [".json"]:
        return ImporterJSON(args, filearg)
    logging.getLogger('stderr').error(f"No supported importer found for {_ext}\n")
    return Importer(args, None)
