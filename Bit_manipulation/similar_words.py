# xxypp
# aabyy

SAME PATTREN OF LETTERS 
IN ABOVE 
xx : aa
y : b
pp : yy

using hashing we can assign for each character different

def iso(s1,s2):
  Dict = {}
  ndup = []
  for i in range(len(s1)):
     if s1[i] not in ndup:
        ndup.append(s1[i])
        Dict[s1[i]] = s2[i]
     elif Dict[s1[i]] != s2[i]:
        return False
  return True
print(iso(input(),input()))

        





