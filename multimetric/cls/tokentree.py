# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib

import logging
from enum import Enum
from typing import List
from typing import Tuple


class TokenTreeConfig():

    def __init__(self,
                 start: List[Tuple[str, str]],
                 end: List[Tuple[str, str]],
                 needle: List[str],
                 trim: List[str]) -> None:
        self.start = start
        self.end = end
        self.needle = needle
        self.trim = trim

    def match(self, token, config_item: List[Tuple[str, str]]) -> bool:
        for item in config_item:
            type_, val = item
            if str(token[0]).startswith(str(type_)) and (val == token[1] or not val):
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
        for _, value in iterator:
            if state == TokenTree.TreeState.START:
                if config.match(value, config.start):
                    logging.getLogger('stderr').debug(f'Match start: {value}')
                    state = TokenTree.TreeState.INBLOCK
            elif state == TokenTree.TreeState.INBLOCK:
                if config.match(value, config.end):
                    logging.getLogger('stderr').debug(f'Match end: {value}')
                    state = TokenTree.TreeState.START
                    if last_hit:
                        result.add(' '.join(last_hit))
                    last_hit = []
                if any(str(value[0]).startswith(x) for x in config.needle):
                    logging.getLogger('stderr').debug(f'Match needle: {value}')
                    _extracted_value = value[1]
                    for i in config.trim:
                        _extracted_value = _extracted_value.strip(i)
                    if _extracted_value:
                        last_hit.append(_extracted_value)
                elif str(value[0]) in ['Token.Text.Whitespace'] and value[1].strip(' ').endswith('\n'):
                    logging.getLogger('stderr').debug(f'Inblock line end: {value} -> {last_hit}')
                    if last_hit:
                        result.add(' '.join(last_hit))
                    last_hit = []
        logging.getLogger('stderr').debug(f'Found {result}')
        return result
