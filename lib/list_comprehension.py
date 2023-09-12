#!/usr/bin/env python3

def return_evens(num_list):
    even_list = [num for num in num_list if num % 2 == False]
    return even_list

def make_exclamation(sentence_list):
    excited_sentence = [sentence + "!" for sentence in sentence_list]
    return excited_sentence