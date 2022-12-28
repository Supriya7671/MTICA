string='''practice problems for List com pre hension in pythopn.'''
wordsLst=string.split(' ')
##print(wordsLst)
wordsLst=[i.strip("\n") for i in wordsLst]
##print(wordsLst)
ans={i:i[::-1]for i in wordsLst}
print(ans)
