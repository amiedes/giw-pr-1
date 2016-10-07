# -*- coding: utf-8 -*-
"""
Created on Thu Oct 06 19:50:08 2016

@author: dany
"""
Max_Size=91
Min_Size=65
Alpha_Size=26

    
def encrypt(word,positions):
    new_word=""
    for letter in word:
        if (letter.isalpha()):
            newPos=positions + ord(letter)
            if (newPos < Max_Size):
                letter=chr(newPos)
            else:
                letter=chr((newPos+Min_Size)%Max_Size)
        new_word+=letter        
    print new_word
    return new_word        
    
def main():
    print "Bienvenido a Cifrado César !!"
    print "Intoduce las palabras que quieres Cifrar:"
    phrase=raw_input()
    phrase=phrase.upper()
    phrase=phrase.split()
    phrase_size=len(phrase)    
    valid=False
    while (not valid):
        try:    
            positions=int(raw_input("Desplazamiento de Letras ?:"))
            positions=positions%Alpha_Size
            movement=int(raw_input("Movimiento por Palabra ?:"))
            movement=movement%phrase_size
            valid=True
        except:
            print "--------------------ERROR--------------------------------"
            print "El Desplazamiento y Movimiento deben ser un Número Entero"
            print "Vuelve a intentarlo:"
            print "---------------------------------------------------------"
            
    new_phrase=[]
    for word in range(len(phrase)):
        new_word=""
        new_word=encrypt(phrase[word],positions)
        new_phrase.append(new_word)    
    #phrase=ch_words(phrase,movement)
    print movement
    print new_phrase

main()    
    
