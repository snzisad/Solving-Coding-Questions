# This program was developed to solve the challenge given by VISMA 
# The task is to find the unique letters that should replace the digits 3, 1, 2, and 0. 
# Every letter shall be assigned a unique base-10 digit value. 
# The letters to be used are V, I, S, M, A, P, H, E, N and L. 
# We have used a simple brute-force algorithm to solve the task.

import itertools

letters = ["V", "I", "S", "M", "A", "P", "H", "E", "N", "L"]
digits = [i for i in range(0, len(letters))]
need_to_find = [3, 1, 2, 0, 3]

# get the list of permutaions of the digits 0 to 9 
permutations = list(itertools.permutations(digits))

# iterate through each permutation
for single_permutaion in permutations:
    letter_to_digit = {}

    # store the digit of a corresponding letter to the dictionary for further operations  
    for i, digit in enumerate(single_permutaion):
        letter_to_digit[letters[i]] = digit

    # check the conditions. If A=1 or M=2, ignore the next operations
    if letter_to_digit["A"] == 1 or letter_to_digit["M"] == 2:
        continue
    
    # get the value of the each part of the equations in string format. So that it can make a perfect number
    VISMA_Value = str(letter_to_digit["V"])+str(letter_to_digit["I"])+str(letter_to_digit["S"])+str(letter_to_digit["M"])+str(letter_to_digit["A"])
    API_Value = str(letter_to_digit["A"])+str(letter_to_digit["P"])+str(letter_to_digit["I"])
    AI_Value = str(letter_to_digit["A"])+str(letter_to_digit["I"])
    SAAS_Value = str(letter_to_digit["S"])+str(letter_to_digit["A"])+str(letter_to_digit["A"])+str(letter_to_digit["S"])
    HEAVEN_Value = str(letter_to_digit["H"])+str(letter_to_digit["E"])+str(letter_to_digit["A"])+str(letter_to_digit["V"])+str(letter_to_digit["E"])+str(letter_to_digit["N"])

    # check the left and right part of the equation
    if int(VISMA_Value)+int(API_Value)+int(AI_Value)+int(SAAS_Value) == int(HEAVEN_Value):
        print(letter_to_digit)

        # print the corresponding letter based on the digits we need to find
        values = list(letter_to_digit.values())
        for digit in need_to_find:
            print(str(digit)+"=>"+letters[values.index(digit)])

        break



