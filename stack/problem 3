def prec(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

def isRightAssociative(c):
    return c == '^'

def infixToPostfix(s):
    st = []
    res = []

    for c in s:
        # If operand, add to result
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
            res.append(c)

        # If '(', push to stack
        elif c == '(':
            st.append('(')

        # If ')', pop until '('
        elif c == ')':
            while st and st[-1] != '(':
                res.append(st.pop())
            st.pop()

        # If operator
        else:
            while st and st[-1] != '(' and \
                (prec(st[-1]) > prec(c) or (prec(st[-1]) == prec(c) \
                                    and not isRightAssociative(c))):
                res.append(st.pop())
            st.append(c)

    # Pop remaining operators
    while st:
        res.append(st.pop())

    return ''.join(res)

if __name__ == '__main__':
    exp = "a*(b+c)/d"
    print(infixToPostfix(exp))