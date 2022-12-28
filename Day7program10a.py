m=[[1,2],[3,4],[5,6],[7,8]]
ans=[[m[col][row]for col in range(len(m))]for row in range(len(m[0]))]
#ans.append(m[col][row]for col in range(len(m)])
##for row in range(len(m[0])):
##    temp=[m[col][row]for col in range(len(m))]
####    for col in range(len(m)):
####        temp.append(m[col][row])
##    ans.append(temp)
print(ans)




