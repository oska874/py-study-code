import cPickle,pprint

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
cPickle.dump(data1, output)

# Pickle the list using the highest protocol available.
cPickle.dump(selfref_list, output, -1)

output.close()

pkl_file = open('data.pkl', 'rb')

data1 = cPickle.load(pkl_file)
print("print: ",data1)
pprint.pprint(data1)

data2 = cPickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()