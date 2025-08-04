# Input: s = "leetcode"
# Output: 0
# Explanation:
# The character 'l' at index 0 is the first character that does not occur at any other index.
def firstUniqChar(s):
    freq_map = {}
    
    for ch in s:
        if ch in freq_map:
            freq_map[ch] += 1
        else:
            freq_map[ch] = 1
    
    for idx, ch in enumerate(s):
        if freq_map[ch] == 1:
            return idx
    
    return -1


s = "leetcode"
print(firstUniqChar(s))
