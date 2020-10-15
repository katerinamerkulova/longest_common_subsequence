"""
Longest common subsequence implementation starter
"""

import main
from tokenizer import tokenize


def test_till_calculate_plagiarism_score():
    origin_text = 'the big cat is sleeping'
    susp_text = 'the cat is big'

    origin_tokens = tokenize(origin_text)
    susp_tokens = tokenize(susp_text)

    print(f'Raw text: {origin_text}')
    print(f'Tokenized text: {origin_tokens}')

    lcs_lenght = main.find_lcs_length(origin_tokens, susp_tokens)
    print('A length of the longest common subsequence for '
        f'{origin_text.upper()} and {susp_text.upper()}: {lcs_lenght}')

    matrix = main.fill_lcs_matrix(origin_tokens, susp_tokens)
    longest_lcs = main.find_lcs(origin_tokens, susp_tokens, matrix)
    print(f'The longest common subsequence: {longest_lcs}')

    score = main.calculate_plagiarism_score(lcs_lenght, susp_tokens)
    print(f'The plagiarism score: {score:.2f}')
    
    

def test_calculate_text_plagiarism_score():
    origin_text = '''the cat is big
the sun is beatiful
the moon is rising'''.split('\n')
    
    susp_text = '''the big cat
the beatiful sun was rising 
a moon will rise'''.split('\n')

    origin_tokens = tokenize_by_lines(origin_text)
    susp_tokens = tokenize_by_lines(susp_text)
    
    while len(origin_text) < len(susp_text):
        origin_text += ('',)

    score = main.calculate_text_plagiarism_score(origin_tokens,
                                                 susp_tokens)

    print(f'The text plagiarism score: {score:.2f}')




test_till_calculate_plagiarism_score()
test_calculate_text_plagiarism_score()