# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    result = 0
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))
            result = result + 1
            pass
        if next in ")]}":
            if opening_brackets_stack == 0 or result == 0:
                return 1
            # Check, if not empty 
            elif result > 0 and are_matching(opening_brackets_stack[result - 1].char, next):
                opening_brackets_stack.pop()
                result = result - 1
            else:
                return i + 1
        pass
        if (len(opening_brackets_stack == 0) or result == 0):
            return 'Success'
        else:
            return opening_brackets_stack[-1].position + 1
           
def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()

