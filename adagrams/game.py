from random import randint
LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

available_letters = [
    {'letter': 'A', 'is_not_available': False},
    {'letter': 'A', 'is_not_available': False},
    {'letter': 'A', 'is_not_available': False},
    {'letter': 'A', 'is_not_available': False},
    {'letter': 'A', 'is_not_available': False},
    {'letter': 'A', 'is_not_available': False},
    {'letter': 'A', 'is_not_available': False},
    {'letter': 'A', 'is_not_available': False},
    {'letter': 'A', 'is_not_available': False},
    {'letter': 'B', 'is_not_available': False},
    {'letter': 'B', 'is_not_available': False},
    {'letter': 'C', 'is_not_available': False},
    {'letter': 'C', 'is_not_available': False},
    {'letter': 'D', 'is_not_available': False},
    {'letter': 'D', 'is_not_available': False},
    {'letter': 'D', 'is_not_available': False},
    {'letter': 'D', 'is_not_available': False},
    {'letter': 'E', 'is_not_available': False},
    {'letter': 'E', 'is_not_available': False},
    {'letter': 'E', 'is_not_available': False},
    {'letter': 'E', 'is_not_available': False},
    {'letter': 'E', 'is_not_available': False},
    {'letter': 'E', 'is_not_available': False},
    {'letter': 'E', 'is_not_available': False},
    {'letter': 'E', 'is_not_available': False},
    {'letter': 'E', 'is_not_available': False},
    {'letter': 'E', 'is_not_available': False},
    {'letter': 'E', 'is_not_available': False},
    {'letter': 'E', 'is_not_available': False},
    {'letter': 'F', 'is_not_available': False},
    {'letter': 'F', 'is_not_available': False},
    {'letter': 'G', 'is_not_available': False},
    {'letter': 'G', 'is_not_available': False},
    {'letter': 'G', 'is_not_available': False},
    {'letter': 'H', 'is_not_available': False},
    {'letter': 'H', 'is_not_available': False},
    {'letter': 'I', 'is_not_available': False},
    {'letter': 'I', 'is_not_available': False},
    {'letter': 'I', 'is_not_available': False},
    {'letter': 'I', 'is_not_available': False},
    {'letter': 'I', 'is_not_available': False},
    {'letter': 'I', 'is_not_available': False},
    {'letter': 'I', 'is_not_available': False},
    {'letter': 'I', 'is_not_available': False},
    {'letter': 'I', 'is_not_available': False},
    {'letter': 'J', 'is_not_available': False},
    {'letter': 'K', 'is_not_available': False},
    {'letter': 'L', 'is_not_available': False},
    {'letter': 'L', 'is_not_available': False},
    {'letter': 'L', 'is_not_available': False},
    {'letter': 'L', 'is_not_available': False},
    {'letter': 'M', 'is_not_available': False},
    {'letter': 'M', 'is_not_available': False},
    {'letter': 'N', 'is_not_available': False},
    {'letter': 'N', 'is_not_available': False},
    {'letter': 'N', 'is_not_available': False},
    {'letter': 'N', 'is_not_available': False},
    {'letter': 'N', 'is_not_available': False},
    {'letter': 'N', 'is_not_available': False},
    {'letter': 'O', 'is_not_available': False},
    {'letter': 'O', 'is_not_available': False},
    {'letter': 'O', 'is_not_available': False},
    {'letter': 'O', 'is_not_available': False},
    {'letter': 'O', 'is_not_available': False},
    {'letter': 'O', 'is_not_available': False},
    {'letter': 'O', 'is_not_available': False},
    {'letter': 'O', 'is_not_available': False},
    {'letter': 'P', 'is_not_available': False},
    {'letter': 'P', 'is_not_available': False},
    {'letter': 'Q', 'is_not_available': False},
    {'letter': 'R', 'is_not_available': False},
    {'letter': 'R', 'is_not_available': False},
    {'letter': 'R', 'is_not_available': False},
    {'letter': 'R', 'is_not_available': False},
    {'letter': 'R', 'is_not_available': False},
    {'letter': 'R', 'is_not_available': False},
    {'letter': 'S', 'is_not_available': False},
    {'letter': 'S', 'is_not_available': False},
    {'letter': 'S', 'is_not_available': False},
    {'letter': 'S', 'is_not_available': False},
    {'letter': 'T', 'is_not_available': False},
    {'letter': 'T', 'is_not_available': False},
    {'letter': 'T', 'is_not_available': False},
    {'letter': 'T', 'is_not_available': False},
    {'letter': 'T', 'is_not_available': False},
    {'letter': 'T', 'is_not_available': False},
    {'letter': 'U', 'is_not_available': False},
    {'letter': 'U', 'is_not_available': False},
    {'letter': 'U', 'is_not_available': False},
    {'letter': 'U', 'is_not_available': False},
    {'letter': 'V', 'is_not_available': False},
    {'letter': 'V', 'is_not_available': False},
    {'letter': 'W', 'is_not_available': False},
    {'letter': 'W', 'is_not_available': False},
    {'letter': 'X', 'is_not_available': False},
    {'letter': 'Y', 'is_not_available': False},
    {'letter': 'Y', 'is_not_available': False},
    {'letter': 'Z', 'is_not_available': False}
]

def draw_letters():
    letter_bank = []

    while len(letter_bank) < 10:
        index_of_letter = get_index_of_letter()

        # Check to see if the letter is available
        if not available_letters[index_of_letter]['is_not_available']:
            letter_bank.append(available_letters[index_of_letter]['letter'])
            # The letter is_not_available so change the value to True
            available_letters[index_of_letter]['is_not_available'] = True

    # Reset letters in available letters
    reset_available_letters(available_letters)

    return letter_bank

def uses_available_letters(word, letter_bank):
    letters_in_word = list(word.upper())
    
    is_valid = False

    for letter in word:
        if word.count(letter) > 0 and \
           letters_in_word.count(letter) <= letter_bank.count(letter):
            continue
        else:
            return is_valid
    
    is_valid = True

    return is_valid

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

def get_index_of_letter():
    return randint(0, len(available_letters) - 1)

def reset_available_letters(available_letters):
    for letter in range(len(available_letters)):
        available_letters[letter]['is_not_available'] = False

print(draw_letters())