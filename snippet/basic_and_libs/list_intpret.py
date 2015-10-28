m=[[1,2,3],
[4,5,6],
[7,8,9]
]

print(m)

c=[m[row][col] for row in range(3) for col in range(3)]
print(c)
c=[[m[row][col] for row in range(3)] for col in range(3)]
print(c)


ll=[line.rstrip() for line in open('gui_0.py')]
print(ll)