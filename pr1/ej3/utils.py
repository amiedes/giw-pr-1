# -*- coding: utf-8 -*-

'''
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
'''

import string

def spanish_tolower(word):
    lowered_word = ''
    for letter in word:
        if letter == 'Á':
            lowered_word += 'á'
        elif letter == 'É':
            lowered_word += 'é'
        elif letter == 'Í':
            lowered_word += 'í'
        elif letter == 'Ó':
            lowered_word += 'ó'
        elif letter == 'Ú':
            lowered_word += 'ú'
        elif letter == 'Ñ':
            lowered_word += 'ñ'
        else:
            lowered_word += letter.lower()
    return lowered_word

def clean_word(word):
    clean_word = ''
    for letter in word:
        if (letter in string.ascii_letters) or (letter in 'ÁáÉéÍíÓóÚúñÑ'):
            clean_word += spanish_tolower(letter)
    return clean_word

def write_dictionary_to_file(dictionary, output_file_name = "output.txt"):
    fh = open(output_file_name, 'w')
    for word in dictionary:
        fh.write(word + ' ' + str(dictionary[word]) + '\n')
    fh.close()

def process_file(filename):
    if (filename == ''): filename = 'input.txt'
    # open file and get file handler
    fh = open(filename)
    # create empty dictionary for storing words
    dictionary = dict()
    # process each line in the file
    for line in fh:
        words = line.split(' ')
        # process each word in the line
        for word in words:
            word = clean_word(word)
            if word in dictionary:
                dictionary[word] += 1
            elif word != '':
                dictionary[word] = 1
    fh.close()
    # write dictionary into output file
    write_dictionary_to_file(dictionary)
