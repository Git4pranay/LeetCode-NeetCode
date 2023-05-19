# d = input()
# f = d
# ds = input()
# d += '0'*(len(ds)-1)
# def x(a,b):
#     return ''.join([ '0' if a[i]==b[i] else '1' for i in range(len(b)) ])[1:]
#     # s= ''
#     # for i in range(len(b)):
#     #     if a[i]==b[i]:
#     #         s+='0'
#     #     else:
#     #         s+='1'
#     # return s[1:]
# print(x('1001','1101'))
# def crc(d,ds):
#     i = len(ds)
#     ans = x(d[:4],ds) + d[i]
#     while (i < len(d)-1):
#         i += 1
#         if ans[0] == '1':
#             ans = x(ans,ds) + d[i]
#         else:
#             ans = x(ans,'0'*len(ds)) + d[i]
#     if ans[0] == '1':
#         ans = x(ans,ds)
#     else:
#         ans = x(ans,'0'*len(ds))
#     return ans
# print('remainnder before decode',crc(d,ds))
# f += crc(d,ds)
# print('remainder after decode:',crc(f,ds))
# if '1' in crc(f,ds):
#     print('error')
# else:
#     print('no error')







s=input()
l=[]
a=0
for i in range(len(s)):
    if (i+1)%8==0:
         l.append(s[a:i+1])
         a=i+1

print(l)

