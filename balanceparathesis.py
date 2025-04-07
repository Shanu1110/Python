def is_balanced(expression):
    stack = []
    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            top = stack.pop()
            if (char == ")" and top != "(") or \
               (char == "]" and top != "[") or \
               (char == "}" and top != "{"):
                return False
    return not stack     