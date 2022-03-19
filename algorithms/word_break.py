# Given a string s and a dictionary of strings wordDict, return true if
# s can be segmented into a space-separated sequence of one or more
# dictionary words.
#
# Note that the same word in the dictionary may be reused multiple
# times in the segmentation.
#
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
#
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true

# Constraints:
# - 1 <= s.length <= 300
# - 1 <= wordDict.length <= 1000
# - 1 <= wordDict[i].length <= 20
# - s and wordDict[i] consist of only lowercase English letters.
# - All the strings of wordDict are unique.

def word_break(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                dp[i] = dp[i + len(w)]

            if dp[i]:
                break

    return dp[0]
