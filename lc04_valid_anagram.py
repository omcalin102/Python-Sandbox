def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    counts = {}
    
    for letter in s:
        counts[letter] = counts.get(letter, 0) + 1
    
    for letter in t:
        if letter not in counts:
            return False
        
        
        counts[letter] -= 1
        
        if counts[letter] < 0:
            return False
        
    return True
    
        
        
print(is_anagram("listen", "silent"))