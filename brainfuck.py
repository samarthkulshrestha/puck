#!/usr/bin/python
#
# Brainfuck Interpreter
# by Samarth Kulshrestha
#
# Usage: ./brainfuck.py <file>
# or python brainfuck.py <file>

import sys
import get_char

def execute_file(filename):
    with open(filename, "r") as f:
        evaluate_code(f.read())


def evaluate_code(code):
    code = cleanup(list(code))
    bracemap = build_bracemap(code)

    cells, codeptr, cellptr = [0], 0, 0

    while codeptr < len(code):
        command = code[codeptr]

        if command == ">":
            cellptr += 1
            if cellptr == len(cells): cells.append(0)

        if command == "<":
            cellptr = 0 if cellptr <= 0 else cellptr - 1

        if command == "+":
            cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

        if command == "-":
            cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

        if command == "[" and cells[cellptr] == 0: codeptr = bracemap[codeptr]
        if command == "]" and cells[cellptr] != 0: codeptr = bracemap[codeptr]
        if command == ".": sys.stdout.write(chr(cells[cellptr]))
        if command == ",": cells[cellptr] = ord(get_char.get_char())

        codeptr += 1


def cleanup(code):
    return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))


def build_bracemap(code):
    temp_bracestack, bracemap = [], {}

    for position, command in enumerate(code):
        if command == "[": temp_bracestack.append(position)
        if command == "]":
            start = temp_bracestack.pop()
            bracemap[start] = position
            bracemap[position] = start
    return bracemap


def main():
    if len(sys.argv) == 2: execute_file(sys.argv[1])
    else: print("Usage:", sys.argv[0], "filename")

if __name__ == "__main__": main()

