# python 3
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(txt):
    opening_brackets_stack = []
    result = 0
    for i, next in enumerate(txt):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))
            result = result + 1
            pass
        if next in ")]}":
            if opening_brackets_stack == 0 and result == 0:
                return 1
            elif result > 0 and are_matching(opening_brackets_stack[result - 1].char, next):
                opening_brackets_stack.pop()
                result = result - 1
            else:
                return i + 1
        pass
    if opening_brackets_stack == 0 or result == 0:
        return 'Success'
    else:
        return opening_brackets_stack[-1].position + 1

def main():
    txt = input()
    if txt[0] == 'I':
        txt = input()
        mismatch = find_mismatch(txt)
        print(mismatch)
    else:
        print('Incorrect type of input')

if __name__ == "__main__":
    main()

