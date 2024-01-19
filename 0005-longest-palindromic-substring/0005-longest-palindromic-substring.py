class Solution:
    def longestPalindrome(self, s: str) -> str:
     longest = ''
     n = len(s)
     for i in range(n):
         for j in range(i+1,n+1):
             word = s[i:j]
             if word == word[::-1]:
                 if len(word)>len(longest):
                     longest = word          
     return longest
        