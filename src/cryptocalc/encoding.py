# -*- coding: utf-8 -*-
"""
Created on Sat May 19 10:57:00 2018

@author: raul
"""


def encode(sentence):
    encoded_sentence = 0
    for n in range(len(sentence)):
        encoded_sentence += ord(sentence[n])*(256**n)
    return encoded_sentence


def decode(encoded_sentence):
    decoded_sentence = ""
    while encoded_sentence != 0:
        decoded_sentence += chr(encoded_sentence % 256)
        encoded_sentence = encoded_sentence//256
    return decoded_sentence
