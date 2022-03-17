# Given two strings s and t, return true if t is an anagram of s, and 
# false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters 
# exactly once.

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    letters_s, letters_t = {}, {}
    for i in range(len(s)):
        letters_s[s[i]] = letters_s.get(s[i], 0) + 1
        letters_t[t[i]] = letters_t.get(t[i], 0) + 1
    return letters_s == letters_t