# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib

import logging
import re
from enum import Enum
from typing import List
from typing import Tuple


class TokenTreeConfig():

    def __init__(self,
                 start: List[Tuple[str, str]],
                 end: List[Tuple[str, str]],
                 needle: List[str],
                 trim: List[str],
                 include_start: bool = False,
                 split_by: str = None) -> None:
        self.start = start
        self.end = end
        self.needle = needle
        self.trim = trim
        self.include_start = include_start
        self.split_by = split_by

    def match(self, token, config_item: List[Tuple[str, str]]) -> bool:
        for item in config_item:
            type_, value = item
            if str(token[0]).startswith(str(type_)) and (re.match(value, token[1]) or not value):
                return True
        return False


class TokenTree():
    class TreeState(Enum):
        START = 0
        INBLOCK = 1

    @staticmethod
    def get_from_token_tree(iterator, config: TokenTreeConfig) -> List[str]:
        state = TokenTree.TreeState.START
        result = set()
        last_hit = []

        def cleanup(item: str, config: TokenTreeConfig) -> str:
            for i in config.trim:
                if len(i) == 1:  # pragma: no cover - bug in pytest-cov
                    item = item.strip(i)  # pragma: no cover - bug in pytest-cov
                else:  # pragma: no cover - bug in pytest-cov
                    item = item.replace(i, '')  # pragma: no cover - bug in pytest-cov
            return item

        def merge(list_: List[str], res: set, config: TokenTreeConfig) -> None:
            if not list_:
                return  # pragma: no cover
            if config.split_by:
                res.update(' '.join(list_).split(config.split_by))  # pragma: no cover - bug in pytest-cov
            else:
                res.add(' '.join(list_))

        for _, value in iterator:
            if state == TokenTree.TreeState.START:
                if config.match(value, config.start):
                    logging.getLogger('stderr').debug(f'Match start: {value}')
                    if config.include_start:
                        item = cleanup(value[1], config)  # pragma: no cover - bug in pytest-cov
                        if item:  # pragma: no cover
                            logging.getLogger('stderr').debug(f'Adding chunk: {item}')
                            last_hit.append(item)
                    state = TokenTree.TreeState.INBLOCK
            elif state == TokenTree.TreeState.INBLOCK:  # pragma: no cover - bug in pytest-cov
                if config.match(value, config.end):
                    logging.getLogger('stderr').debug(f'Match end: {value}')
                    state = TokenTree.TreeState.START
                    merge(last_hit, result, config)
                    last_hit = []
                if any(str(value[0]).startswith(x) for x in config.needle):
                    logging.getLogger('stderr').debug(f'Match needle: {value}')
                    item = cleanup(value[1], config)
                    if item:
                        logging.getLogger('stderr').debug(f'Adding chunk: {item}')
                        last_hit.append(item)
                elif str(value[0]) in ['Token.Text.Whitespace'] and value[1].strip(' ').endswith('\n'):
                    logging.getLogger('stderr').debug(f'Inblock line end: {value} -> {last_hit}')
                    merge(last_hit, result, config)
                    last_hit = []
        logging.getLogger('stderr').debug(f'Found {result}')
        return result
