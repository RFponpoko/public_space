# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 17:12:30 2022

@author: Hiroaki.Kato
"""

"""
num = number you want to check
n = nth bit (from 0)
MSB to LSB
"""

def is_nth_bit_set(num: int, n: int):
    if num & (1 << n):
        return True
    return False


def bit_checker(data):

    for _ in range(len(bin(data))-2):
        if (is_nth_bit_set(data, _)) == True:
            print(_, "bit:1", sep='')
        else:
            print(_, "bit:0", sep='')

if __name__ == '__main__':

    # example
    bit_checker(128)