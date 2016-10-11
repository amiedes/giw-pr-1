# -*- coding: utf-8 -*-

"""
Created on Thu Oct 06 19:50:08 2016
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

'''
Considerar un sistema de cifrado en el que se sustituye cada letra en el texto
original por otra letra que se encuentra un número fijo de posiciones más adelante
en el alfabeto. Por ejemplo si el desplazamiento es 3 posiciones, y se considera
la letra A, entonces sería sustituida por la letra D que se encuentra situada 3
lugares a la derecha de la A. Se considera que el alfabeto es circular por lo que
a continuación de la Z comienza la letra A. Sólo se codifican las letras, el resto
de símbolos se mantienen tal cual. A continuación, una vez cifrado el texto, si
éste contiene más de una palabra, entonces se reordenan las palabras cifradas,
moviendo cada palabra m posiciones hacia la derecha. Así la palabra que ocupa la
posición 1 se mueve a la posición m+1, y así sucesivamente (la palabra que ocupa
la posición n se moverá a la posición m). Se pide implementar un programa en Python
que solicite al usuario que introduzca por teclado un texto a codificar, dos números
que representan el desplazamiento de letras y el desplazamiento de las palabras
codificadas. Como resultado, el programa mostrará por pantalla el mensaje
codificado. Se deben hacer las comprobaciones necesarias sobre la entrada, es
decir que es una cadena y 2 números.
'''

from collections import deque

MAX_SIZE = 91
MIN_SIZE = 65
ALPHABET_SIZE = 26


def shift_letters_right(word, letter_shift):
    new_word = ""
    for letter in word:
        if (letter.isalpha()):
            newPos = letter_shift + ord(letter)
            if (newPos < MAX_SIZE):
                letter = chr(newPos)
            else:
                letter = chr((newPos + MIN_SIZE) % MAX_SIZE)
        new_word += letter
    return new_word

def main():
    print "Bienvenido a Cifrado César !!"
    print "Intoduce las palabras que quieres Cifrar:"

    phrase = raw_input()
    phrase = phrase.upper()
    phrase = phrase.split()
    phrase_size = len(phrase)

    valid = False
    while (not valid):
        try:
            letter_shift = int(raw_input("Desplazamiento de Letras ?:"))
            letter_shift = letter_shift % ALPHABET_SIZE
            word_shift = int(raw_input("Movimiento por Palabra ?:"))
            word_shift = word_shift % phrase_size
            valid = True
        except:
            print "--------------------ERROR--------------------------------"
            print "El Desplazamiento y Movimiento deben ser un Número Entero"
            print "Vuelve a intentarlo:"
            print "---------------------------------------------------------"

    new_phrase = []

    # Rotar las letras de cada una de las palabras de la frase
    for word in phrase:
        new_word = ""
        new_word = shift_letters_right(word, letter_shift)
        new_phrase.append(new_word)

    # Rotar las palabras dentro de la frase
    new_phrase = deque(new_phrase)
    new_phrase.rotate(word_shift)

    # Imprimir el resultado
    print ' '.join(new_phrase)

main()
