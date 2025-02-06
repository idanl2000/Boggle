##############################################################################
# FILE: utils.py
# WRITER: Idan Lieberman
# DESCRIPTION:A helper file for ex11 with the founciton that are mandtory
##############################################################################
import boggle_board_randomizer



from typing import List, Tuple, Iterable, Optional

Board = List[List[str]]
Path = List[Tuple[int, int]]


def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:

    pev_row, pev_col = path[0]
    word = ""
    for loc in path:
        row, col = loc
        if -1 <= pev_col - col <= 1 and -1 <= pev_row - row <= 1:
            word += board[row][col]
        else:
            return None
        pev_row, pev_col = row, col
    if word in words:
        return word
    return None



def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:

    path_list= []
    for row in range(len(board)):
        for col in range(len(board[row])):
            _find_length_n_paths_halper(n - 1, board, words, '', row, col, [], path_list)

    return path_list


def _find_length_n_paths_halper(n: int, board: Board, words: Iterable[str],
                                word: str, row: int, col: int, path: Path, path_list: list[Path]):

    if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or (row,col) in path:
        return

    path.append((row, col))
    word = word + board[row][col]

    if n == 0:
        if word in words:
            path_list.append(list(path.copy()))
        path.pop()
        return

    #1
    _find_length_n_paths_halper(n - 1, board, words, word, row - 1, col - 1, path, path_list)
    #2
    _find_length_n_paths_halper(n - 1, board, words, word, row - 1, col, path, path_list)
    #3
    _find_length_n_paths_halper(n - 1, board, words, word, row - 1, col + 1, path, path_list)
    #4
    _find_length_n_paths_halper(n - 1, board, words, word, row, col - 1, path, path_list)
    #5
    _find_length_n_paths_halper(n - 1, board, words, word, row, col + 1, path, path_list)
    #6
    _find_length_n_paths_halper(n - 1, board, words, word, row + 1, col - 1, path, path_list)
    #7
    _find_length_n_paths_halper(n - 1, board, words, word, row + 1, col, path, path_list)
    #8
    _find_length_n_paths_halper(n - 1, board, words, word, row + 1, col + 1, path, path_list)
    path.pop()


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:

    path_list = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            _find_length_n_paths_halper(n - 1, board, words, '', row, col, [], path_list)

    return path_list

def _max_score_halper(n: int, board: Board, words: Iterable[str]) -> List[Path]:

    path_dict= {}
    for row in range(len(board)):
        for col in range(len(board[row])):
            _max_score_halper_halper(n - 1, board, words, '', row, col, [], path_dict)
    return path_dict


def _max_score_halper_halper(n: int, board: Board, words: Iterable[str],
                                word: str, row: int, col: int, path: Path, path_dict: dict[str: Path]):

    if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or (row,col) in path:
        return

    path.append((row, col))
    word = word + board[row][col]

    if n == 0:
        if word in words and word not in path_dict.keys():
            path_dict[word] = list(path.copy())
        path.pop()
        return

    #1
    _max_score_halper_halper(n - 1, board, words, word, row - 1, col - 1, path, path_dict)
    #2
    _max_score_halper_halper(n - 1, board, words, word, row - 1, col, path, path_dict)
    #3
    _max_score_halper_halper(n - 1, board, words, word, row - 1, col + 1, path, path_dict)
    #4
    _max_score_halper_halper(n - 1, board, words, word, row, col - 1, path, path_dict)
    #5
    _max_score_halper_halper(n - 1, board, words, word, row, col + 1, path, path_dict)
    #6
    _max_score_halper_halper(n - 1, board, words, word, row + 1, col - 1, path, path_dict)
    #7
    _max_score_halper_halper(n - 1, board, words, word, row + 1, col, path, path_dict)
    #8
    _max_score_halper_halper(n - 1, board, words, word, row + 1, col + 1, path, path_dict)
    path.pop()


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:

    path_dict = {}
    n = 3
    l = _max_score_halper(n, board, words)
    while l:
        n += 1
        if l:
            for key in l:
                path_dict[key] = l[key]
        l = _max_score_halper(n, board, words)
    return list(path_dict.values())









