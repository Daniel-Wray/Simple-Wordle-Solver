# -*- coding: utf-8 -*-
'''
Simple Wordle Code solver.

If you are missing the "words_fiveLetters.txt", run "wordlist creator.py" on my page.
I suppose you could also replace it with your own list if you have one.

@author: Daniel Wray
'''

'''
The initial set up is asking for inputs of the green positions,
the yellow letters and their positions,
the gray letters,
and whether or not you want the code to return only words in the wordlist.
'''

only_real_words = input('''Return a list of only words in the wordlist or all permutations?
          (Please enter '1' or '2' respectively.) ''')
if only_real_words not in ['1', '2']: raise ValueError("Please enter '1' or '2' exactly!")
if only_real_words == '1' : only_real_words = True
elif only_real_words == '2': only_real_words = False

green_positions = []
for x in range(5):
    y = input('Enter the green letter in position ' + str(x + 1) + '.'
          '\nIf the letter is unknown, simply press enter and skip. ')
    if (len(y) == 1 and y.isalpha()) or len(y) == 0:
        green_positions.append(y.lower())
    else: raise ValueError("Please enter a single alphabetic character or nothing at all.")

yellow = input('''Enter all yellow letters in any order. 
               \nIf there are no revealed yellow characters, simply press enter and skip. ''')
if len(yellow) > 5: raise ValueError("Maximum five characters. This is a wordle solver!")
if len(yellow) != 0 and yellow.isalpha() == False : raise ValueError('Only alphabetic characters!')

yellow_positions = []
if len(yellow) != 0:
    for x in range(5):
        y = input('Enter the yellow letter(s) in position ' + str(x + 1) + '.'
              '\nNo spaces. If there are no letters, simply press enter and skip. ')
        if (y.isalpha()) or len(y) == 0:
            yellow_positions.append(y.lower())
        else: raise ValueError("Please enter alphabetic characters or nothing at all.")
        # I do not check to make sure that the yellow characters are used here.
        # Possible source of error but afaik it will not affect the output.
else: yellow_positions = ["","","","",""]

gray = input('''Enter all gray letters in any order. 
               \nIf there are no revealed gray characters, simply press enter and skip. ''')
if len(gray) != 0 and gray.isalpha() == False : raise ValueError('Only alphabetic characters!')

'''
The rest of the code deals with
getting the wordlist ready,
setting up the possible letters for each position, 
and then going through possible words and printing them.
'''

if only_real_words == True:
    filename = "words_fiveLetters.txt"
    with open(filename, encoding='utf-8') as f:
        wordlist = f.read()
    
    wordlist_words = list(wordlist.split())

alphas = [chr(i) for i in range(ord('a'),ord('z')+1)]

invalid = {}
for index, position in enumerate(yellow_positions, start = 1):
    invalid[index] = list(gray) + list(position)

valid = {}
for index, position in enumerate(green_positions, start = 1):
    if position != "":
        valid[index] = position
    else: valid[index] = [i for i in alphas if i not in invalid[index]]


valid_words = list()
for let_1 in valid[1]:
    for let_2 in valid[2]:
        for let_3 in valid[3]:
            for let_4 in valid[4]:
                for let_5 in valid[5]:
                    new_word = let_1 + let_2 + let_3 + let_4 + let_5
                    if set(yellow).issubset(list(new_word)):
                        if only_real_words == True:
                            if new_word in wordlist_words:
                                print(new_word)
                                valid_words.append(new_word)
                        else: print(new_word); valid_words.append(new_word)
                        
#valid_words is the list of words printed, if you would like to use it.