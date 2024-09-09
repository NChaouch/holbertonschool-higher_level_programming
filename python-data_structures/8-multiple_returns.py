#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    first_char = None if leng == 0 else sentence[0]
    return (leng, first_char)
