
fd1 = open('test.txt','r')
for i in fd1:
    i = i.strip()
    print(len(i))
    print(i)
    print("\n")
