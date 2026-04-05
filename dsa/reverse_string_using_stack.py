def reverse_string_using_stack(s):
    stack = []
    for char in s:
        stack.append(char)
    reversed_string = ''
    while stack:
        reversed_string = reversed_string + stack.pop()
    return reversed_string

result = reverse_string_using_stack("Hello, World!")
print(result)