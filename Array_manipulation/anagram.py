#check anagram or not ("aaba" == "aaab")
class Solution:
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return 0
        
        dic1 = {}
        for i in range(len(s)):
            if s[i] not in dic1:
                dic1[s[i]]=1
            else:
                dic1[s[i]]+=1
            if t[i] not in dic1:
                dic1[t[i]]=-1
            else:
                dic1[t[i]]-=1
        for i in dic1:
            if dic1[i]!=0:
                return 0
        return 1
# o(n) beats 10%

# using functions in python (count,set)
class Solution:
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return 0
        for i in set(s):
            if s.count(i)!=t.count(i):
                return 0
        return 1
# beats 100%