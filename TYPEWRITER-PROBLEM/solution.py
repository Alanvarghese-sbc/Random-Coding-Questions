def process(s):
    stack = []

    for ch in s:
        if ch == '#':
            if stack:
                stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)


s1 = input().strip()
s2 = input().strip()

if process(s1) == process(s2):
    print("True")
else:
    print("False")