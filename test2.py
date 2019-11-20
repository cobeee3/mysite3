x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
#注意：Python3.x和Python2.x这里的差别
#Python3.x
# xyz = list(zip(x, y, z))
#Python2.x
xyz = zip(x, y, z)
print(xyz)
#输出结果：[(1, 4, 7), (2, 5, 8), (3, 6, 9)]