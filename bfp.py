"""A BrainF*ck interpreter in Python.

This interpreter is for a dialect of BrainF*ck
called BrainF*ck+, which supports all standard
bf commands, plus a `@` command which prints the
index of the current data cell to console. This
is particularly helpful for debugging code.
"""

import sys

with open(sys.argv[1], 'r') as f:
    program = f.read()

# print(program, end='\n\n')

program_pointer = 0
array_pointer = 0

program_array = [0]
chars_to_read = ['<', '>', ',', '.', '+', '-', '[', ']']
if len(sys.argv) > 2 and sys.argv[2] in ['--at', '--easy', '-e']: chars_to_read.append('@')

while program_pointer < len(program):
    # if the current char is not one of the eight recognized by the language,
    # go read the next char
    current_char = program[program_pointer]
    if current_char not in chars_to_read: 
        program_pointer += 1
        continue
    
    # print(current_char, end='')

    if current_char == '<':
        # check if it is possible to move back, and then move back the array pointer by 1
        if array_pointer > 0: array_pointer -= 1
        else: raise RuntimeError('You went too far back!')
    
    if current_char == '>':
        # make a new cell and move the array pointer to the right
        program_array.append(0)
        array_pointer += 1

    if current_char == '.':
        # print the contents of the current cell as an ASCII character
        print(chr(program_array[array_pointer]), end='')

    if current_char == ',':
        # read in the input and convert it from ASCII to an int
        program_array[array_pointer] = ord(input('\nbf> '))

    if current_char == '+':
        # increment the value in the current cell, with 8-bit rollover
        if program_array[array_pointer] < 255: program_array[array_pointer] += 1
        else: program_array[array_pointer] = 0  # rollover

    if current_char == '-':
        # decrement the value in the current cell, with 8-bit rollover
        if program_array[array_pointer] > 0: program_array[array_pointer] -= 1
        else: program_array[array_pointer] = 255  # rollover

    if current_char == '[':
        if program_array[array_pointer] == 0:
            # look for the matching `]` and set the array_pointer to the cell after that one
            bracket_counter = 1
            sub_pointer = program_pointer + 1
            while bracket_counter != 0:
                if program[sub_pointer] == '[': bracket_counter += 1
                if program[sub_pointer] == ']': bracket_counter -= 1
                sub_pointer += 1
            program_pointer = sub_pointer - 1

    if current_char == ']':
        if program_array[array_pointer] != 0:
            # look for the matching `[` and set the array_pointer to that cell
            bracket_counter = 1
            sub_pointer = program_pointer - 1
            while bracket_counter != 0:
                if program[sub_pointer] == '[': bracket_counter -= 1
                if program[sub_pointer] == ']': bracket_counter += 1
                sub_pointer -= 1
            program_pointer = sub_pointer

    if '@' in chars_to_read and current_char == '@':
        # prints where I'm @ (at (get it? (I guess that was lame)))
        print(array_pointer, end='')

    program_pointer += 1