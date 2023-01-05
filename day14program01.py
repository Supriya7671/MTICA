##inpl=['papaya','grapes','banana']
##def res_str(a):
##    return a[::-1]
##outl=list(map(res_str,inpl))
##print(inpl)
##print(outl)
def reverseString(s):
    ans=[i[::-1] for i in s]
    return ans
inp=input().split()
print(inp)
print(*reverseString(inp))
