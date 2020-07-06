mat = [[1,2,3],[4,5,6],[9,8,9]]
diag = [ row[i]for i,row in enumerate(mat) ]
diag1= [row[-i]  for i, row in enumerate(mat, start=1)]
print(diag)
print (diag1)

print(abs(sum(diag)-sum(diag1)))
print(sum(diag1))

