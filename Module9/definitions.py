"""
Program: definitions.py
Author: Paul Ford
Last date modified: 06/27/2020
Purpose: testing my module
"""
import Module9.my_definitions as mx

if __name__ == '__main__':
    mx.greeting()
    mx.author()
    mx.print_dict({'A': 'test', 'B': 'test2', 'C': 'test3'})
    mx.print_set((1, 2, 3, 4, 5, 'Hello'))
