# Given two strings s and t, return true if t is an anagram of s, and 
# false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters 
# exactly once.

def is_anagram(s, t):
    letters_s, letters_t = {}, {}
    for letter in s:
        letters_s[letter] = letters_s.get(letter, 0) + 1
    for letter in t:
        letters_t[letter] = letters_t.get(letter, 0) + 1
    return letters_s == letters_t