# -*- coding: utf-8 -*-
'''
5-letter word list maker

@author: Daniel Wray

This creates a str of  5-letter words and saves it as "words_fiveletters.txt".
To be used with my Wordle solver code.
'''

import urllib.request

# Reading the file as a txt document.
filename = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
wordlist = urllib.request.urlopen(filename).read()
wordlist = wordlist.decode('utf-8')

# Removing non-5 letter words
wordlist = wordlist.split()
wordlist = [x for x in wordlist if len(x) == 5]

# Saving as a str
words_five = ""
for x in wordlist:
    words_five = words_five + x + "\n"

# Outputting the str as a .txt file
with open("words_fiveletters.txt", "w") as output:
    output.write(words_five)
