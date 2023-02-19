# 221RDC030, Boriss Zubkovs, RDCP0
# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i+1))
        if next in ")]}":
            if not opening_brackets_stack:
                return i+1
            if not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            
            opening_brackets_stack.pop()

        if opening_brackets_stack:
            return opening_brackets_stack[0].position 
        else: return "Success"

def main():
    text = input("F or I")
    if "F" in text:
        name = input("Enter name: ")
        with open(name, "r", encoding="latin2") as file:
            text=file.read()
        mismatch = find_mismatch(text)
        if mismatch == "Success":
            print("Success")
        else:
            print(mismatch)
    elif "I" in text:
        text = input()
        mismatch = find_mismatch(text)
        if mismatch == "Success":
            print("Success")
        else:
            print(mismatch)

main()