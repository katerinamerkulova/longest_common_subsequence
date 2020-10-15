"""
Longest common subsequence problem
"""

from tokenizer import tokenize


def tokenize_by_lines(text: str) -> tuple:
    """
    Splits a text into sentences, sentences – into tokens,
    converts the tokens into lowercase, removes punctuation
    :param text: the initial text
    :return: a list of sentences with lowercase tokens without punctuation
    e.g. text = 'I have a cat.\nHis name is Bruno'
    --> (('i', 'have', 'a', 'cat'), ('his', 'name', 'is', 'bruno'))
    """
    text = text.lower().split('\n')
    return tuple(tokenize(sent) for sent in text)


def create_zero_matrix(rows: int, columns: int) -> list:
    """
    Creates a matrix rows * columns where each element is zero
    :param rows: a number of rows
    :param columns: a number of columns
    :return: a matrix with 0s
    e.g. rows = 2, columns = 2
    --> [[0, 0], [0, 0]]
    """
    return [[0 for _ in range(columns)] for __ in range(rows)]


def fill_lcs_matrix(first_sentence_tokens: tuple,
                    second_sentence_tokens: tuple) -> list:
    """
    Fills a longest common subsequence matrix using the Needleman–Wunsch algorithm
    :param first_sentence_tokens: a tuple of tokens
    :param second_sentence_tokens: a tuple of tokens
    :return: a lcs matrix
    """
    first = (0,) + first_sentence_tokens
    second = (0,) + second_sentence_tokens

    rows = len(first)
    columns = len(second)

    matrix = create_zero_matrix(rows, columns)

    for i, word1 in enumerate(first[1:], start=1):
      for j, word2 in enumerate(second[1:], start=1):
        if word1 == word2:
          matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1]) + 1
        else:
          matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    return matrix


def find_lcs_length(first_sentence_tokens: tuple,
                    second_sentence_tokens: tuple,
                    plagiarism_threshold=0.3) -> int:
    """
    Finds a length of the longest common subsequence using the Needleman–Wunsch algorithm
    When a length is less than the threshold, it becomes 0
    :param first_sentence_tokens: a tuple of tokens
    :param second_sentence_tokens: a tuple of tokens
    :param plagiarism_threshold: a threshold
    :return: a length of the longest common subsequence
    """
    lcs_length = fill_lcs_matrix(first_sentence_tokens,
                                 second_sentence_tokens)[-1][-1]
    if lcs_length / len(second_sentence_tokens) < plagiarism_threshold:
        return 0
    return lcs_length


def find_lcs(first_sentence_tokens: tuple,
             second_sentence_tokens: tuple,
             lcs_matrix: list) -> tuple:
    """
    Finds the longest common subsequence itself using the Needleman–Wunsch algorithm
    :param first_sentence_tokens: a tuple of tokens
    :param second_sentence_tokens: a tuple of tokens
    :param lcs_matrix: a filled lcs matrix
    :return: the longest common subsequence
    """
    first_tokens = (0,) + first_sentence_tokens
    second_tokens = (0,) + second_sentence_tokens
    
    row = len(first_tokens) - 1
    column = len(second_tokens) - 1

    longest_lcs = []

    while row or column:
        if first_tokens[row] == second_tokens[column]:
            longest_lcs.append(first_tokens[row])
            row -= 1
            column -= 1
        elif lcs_matrix[row - 1][column] > lcs_matrix[row][column - 1]:
            row -= 1
        else:
            column -= 1
    return longest_lcs[::-1]


def calculate_plagiarism_score(lcs_length: int,
                               suspicious_sentence_tokens: tuple
                               )-> float:
    """
    Calculates the plagiarism score
    The score is the lcs length divided by the number of tokens in a suspicious sentence
    :param lcs_length: a length of the longest common subsequence
    :param suspicious_sentence_tokens: a tuple of tokens
    :return: a score from 0 to 1, where 0 means no plagiarism, 1 – the texts are the same
    """
    return lcs_length / len(suspicious_sentence_tokens)


def calculate_text_plagiarism_score(original_text_tokens: tuple,
                                    suspicious_text_tokens: tuple,
                                    plagiarism_threshold=0.3) -> float:
    """
    Calculates the plagiarism score: compares two texts line by line using lcs
    The score is the sum of lcs values for each pair divided by the number of tokens in suspicious text
    At the same time, a value of lcs is compared with a threshold (e.g. 0.3)
    :param original_text_tokens: a tuple of sentences with tokens
    :param suspicious_text_tokens: a tuple of sentences with tokens
    :param plagiarism_threshold: a threshold
    :return: a score from 0 to 1, where 0 means no plagiarism, 1 – the texts are the same
    """

    while len(original_text_tokens) < len(suspicious_text_tokens):
        original_text_tokens += ('',)

    scores = []
    for i in range(len(suspicious_text_tokens)):
        lcs_length = find_lcs_length(original_text_tokens[i],
                                     suspicious_text_tokens[i],
                                     plagiarism_threshold)
        scores.append(calculate_plagiarism_score(
            lcs_length,
            suspicious_text_tokens[i]))
    return sum(scores) / len(suspicious_text_tokens)


def find_diff_in_sentence(original_sentence_tokens: tuple,
                          suspicious_sentence_tokens: tuple,
                          lcs: tuple) -> tuple:
    """
    Finds words not present in lcs.
    :param original_sentence_tokens: a tuple of tokens
    :param suspicious_sentence_tokens: a tuple of tokens
    :param lcs: a longest common subsequence
    :return: a tuple with tuples of indexes
    """
    idx = []
    for index, (first, second) in enumerate(
        zip(original_sentence_tokens, suspicious_sentence_tokens)):
        if first != second:
            idx.append(index)



def accumulate_diff_stats(original_text_tokens: tuple, suspicious_text_tokens: tuple, plagiarism_threshold=0.3) -> dict:
    """
    Accumulates the main statistics for pairs of sentences in texts:
            lcs_length, plagiarism_score and indexes of differences
    :param original_text_tokens: a tuple of sentences with tokens
    :param suspicious_text_tokens: a tuple of sentences with tokens
    :return: a dictionary of main statistics for each pair of sentences
    including average text plagiarism, sentence plagiarism for each sentence and lcs lengths for each sentence
    {'text_plagiarism': int,
     'sentence_plagiarism': list,
     'sentence_lcs_length': list,
     'difference_indexes': list}
    """
    pass


def create_diff_report(original_text_tokens: tuple, suspicious_text_tokens: tuple, accumulated_diff_stats: dict) -> str:
    """
    Creates a diff report for two texts comparing them line by line
    :param original_text_tokens: a tuple of sentences with tokens
    :param suspicious_text_tokens: a tuple of sentences with tokens
    :param accumulated_diff_stats: a dictionary with statistics for each pair of sentences
    :return: a report
    """
    pass


def find_lcs_length_optimized(first_sentence_tokens: list, second_sentence_tokens: list) -> int:
    """
    Finds a length of the longest common subsequence using the Hirschberg's algorithm
    At the same time, if the first and last tokens coincide,
    they are immediately added to lcs and not analyzed
    :param first_sentence_tokens: a list of tokens
    :param second_sentence_tokens: a list of tokens
    :return: a length of the longest common subsequence
    """
    pass

def tokenize_big_file(path_to_file: str) -> tuple:
    """
    Reads, tokenizes and transforms a big file into a numeric form
    :param path_to_file: a path
    :return: a tuple with ids
    """
    pass
