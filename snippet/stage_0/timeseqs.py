from mytimer import timer, repl, reps
import sys


def for_loop():
    res = []
    for x in repl:
        res.append(abs(x))
    return res


def listComp():
    return [abs(x) for x in repl]


def mapCall():
    return map(abs, repl)


def genExpr():
    return list(abs(x) for x in repl)


def genFunc():
    def gen():
        for x in repl:
            yield abs(x)
    return list(gen())

flist = (for_loop, listComp, mapCall, genExpr, genFunc)

print(sys.version)
for y in range(10):
	for x in flist:
		z=timer(x)
		print('%-9s: %.5f ' % 
			(x.__name__,z[0]))
	print("\n")
