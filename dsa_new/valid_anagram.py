# # Brute Force
def valid_anagram(s:str, t:str) -> bool:
    if len(s) != len(t):
        return False
    else:
        return sorted(s) == sorted(t)
    
s = 'anagram'
t = 'nagaram'
print('the two strings are anagram to each other',valid_anagram(s,t))

# # Optimal solution

def valid_anagram(s:str, t:str) -> bool:
    if len(s) != len(t):
        return False
    
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0)+1
        
    for char in t:
        if char not in char_count or char_count[char] == 0:
            return False
        
        char_count[char] -= 1

    return True

s = 'anagram'
t = 'car'
print('the two strings are valid anagrams', valid_anagram(s,t))
