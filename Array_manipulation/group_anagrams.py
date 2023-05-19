# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# we create a hash function for each string
j='abcdefghijklmnopqrstuvwxyz'
mas = {}
for i in range(len(j)):
    mas[j[i]]=i+1
ans = []
s = list(map(str,input().split()))
def has(x):
    l = len(x)
    S=0
    for i in range(l):
        S+=(ord(x[i])%mas[j[i]])
        print(S)
    return S
dic = {}
for i in s:
   o=i
   if i=="":
       i='890'
   
   x=has(i)
   if x not in dic:
       dic[x]=[o]
   else:
       dic[x]+=[o]
for i in dic:
    ans.append(dic[i])
print(ans,dic)

# BEST ANSWER
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()

