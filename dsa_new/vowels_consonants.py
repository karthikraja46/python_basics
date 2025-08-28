def vowels_consonants(s):
    vowels = 'aeiouAEIOU'
    v_count = 0
    c_count = 0

    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1
    
    return v_count, c_count

s = 'programming'
print('vowels and consonants in the particualr string are:', vowels_consonants(s))