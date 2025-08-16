# input - arr = ["h", "e", "l", "l", "o"]
# output - arr = ['o', 'l', 'l', 'e', 'h']


def reverse_string(s):
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    return s

s = ['h', 'e', 'l', 'l', 'o']
print('The reversed string', reverse_string(s))
