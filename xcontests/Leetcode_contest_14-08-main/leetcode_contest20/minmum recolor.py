class Solution:
    def minimumRecolors(self,s,k):
        for i in range(0,len(s),k):
            if s[i:i+k].count("B")>=k:
               return 0
        ans=[]
        for i in range(len(s)):
             s1=s[i:i+k].replace('W','B')
             if len(s1)==k:
                  ans.append(s[i:i+k])
 
        k=[]
        for i in ans:
            k.append(i.count("W"))
        return min(k)