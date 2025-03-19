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
        if word.count(letter) > 0 and letters_in_word.count(letter) <= letter_bank.count(letter):
            continue
        else:
            return is_valid
    
    is_valid = True

    return is_valid

def score_word(word):
    SCORE_CHART = {
        1 : ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
        2 : ['D', 'G'],
        3 : ['B', 'C', 'M', 'P'],
        4 : ['F', 'H', 'V', 'W', 'Y' ],
        5 : ['K'],
        8 : ['J', 'X' ],
        10 : ['Q', 'Z']
    }
    BONUS_POINTS = 8
    score = 0
    word_same_case = word.upper()

    for letter in word_same_case:
        for points, letters in SCORE_CHART.items():
            if letter in letters:
                score += points

    if len(word) >= 7:
        score += BONUS_POINTS

    return score

def get_highest_word_score(word_list):
    # Build 2D list where each element is a 2 item list of word and score
    word_list_with_scores = build_word_list_with_scores(word_list)
    # Initilize variable to track top score
    top_score = 0
    # Initialize list to store multiple top scores
    multiple_top_scores = []
    # Initialize list to store multiple top scores with word length 10
    multiple_10_letter_words = []
    # Initialize variable to track top score word
    top_score_word = ''
    # Loop through 2D list where current score is ['word',score]
    for current_score in word_list_with_scores:
        # Check to see if the score if greater than or equal to the top score
        if current_score[1] >= top_score:
            # Check to see if the score equals the top score
            if current_score[1] == top_score:
                # Increment top score counter
                top_score_count += 1
                # Add current score ['word',score] to list tracking multiple top scores            
                multiple_top_scores.append(current_score)
            # If the score is greater than top_score, set as top score
            top_score = current_score[1]
            # Assign word to top_score_word
            top_score_word = current_score[0]
    # Check if there are multiple top score words
    if len(multiple_top_scores) > 1:
        # Loop through 2D list
        for current_word in multiple_top_scores:
            # Check if the length of the word is 10
            if current_word[0] == 10:
                # Add 10 letter word to list
                multiple_10_letter_words.append(current_word[0])
        # Check if there are multiple 10 letter words    
        if len(multiple_10_letter_words) > 1:
            # Assign the top score word
            top_score_word = multiple_10_letter_words[0]
            # Assign the top score
            top_score = multiple_10_letter_words[1]
    # Return a tuple
    return tuple(top_score, top_score_word)

def get_index_of_letter():
    return randint(0, len(available_letters) - 1)

def reset_available_letters(available_letters):
    for letter in range(len(available_letters)):
        available_letters[letter]['is_not_available'] = False

def build_word_list_with_scores(word_list):
    word_list_with_scores = []

    for word in word_list:
        current_score = score_word(word)
        word_list_with_scores.append([word, current_score])
    
    return word_list_with_scores

# print(build_word_list_with_scores(["AAAAAAAAAA", "BBBBBB"]))
# print(draw_letters())