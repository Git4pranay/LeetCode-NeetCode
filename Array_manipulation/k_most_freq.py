# cant solve in real method

l = list(map(int,input().split()))
k = int(input)
return sorted(set(l),key = lambda x: l.count(i))[::-1][:k]
# beats 5% worst code ever