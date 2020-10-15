"""
Longest common subsequence implementation starter
"""

import main
from tokenizer import tokenize


def test_tokenize():
    origin_text = 'the big cat is sleeping'
    susp_text = 'the cat is big'

    origin_tokens = tokenize(origin_text)
    susp_tokens = tokenize(susp_text)

    print(f'Raw text: {origin_text}')
    print(f'Tokenized text: {origin_tokens}')
    return origin_tokens, susp_tokens


def test_find_lcs_lenght_and_matrix(origin_tokens, susp_tokens):
    lcs_lenght = main.find_lcs_length(origin_tokens, susp_tokens)
    print('A length of the longest common subsequence for '
        f'{origin_text.upper()} and {susp_text.upper()}: {lcs_lenght}')

    matrix = main.fill_lcs_matrix(origin_tokens, susp_tokens)
    longest_lcs = main.find_lcs(origin_tokens, susp_tokens, matrix)
    print(f'The longest common subsequence: {longest_lcs}')

    return lcs_lenght, matrix
   

def test_calculate_text_plagiarism_score():
    origin_text = '''the cat is big\nthe sun is beatiful\nthe moon is rising'''.split('\n')
    susp_text = '''the big cat\nthe beatiful sun was rising\na moon will rise'''.split('\n')
    
    origin_tokens = tokenize_by_lines(origin_text)
    susp_tokens = tokenize_by_lines(susp_text)
    
    while len(origin_text) < len(susp_text):
        origin_text += ('',)

    score = main.calculate_text_plagiarism_score(origin_tokens,
                                                 susp_tokens)

    print(f'The text plagiarism score: {score:.2f}')
    
    return score


origin_tokens, susp_tokens = test_tokenize()
lcs_lenght, matrix = test_find_lcs_lenght_and_matrix(origin_tokens, susp_tokens)
score = test_calculate_text_plagiarism_score()