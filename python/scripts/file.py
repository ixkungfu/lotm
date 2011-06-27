f = open('foo.js', 'w')
f.write('var i = 0;\n')
f.write('var arr = [];\n')
f.writelines('arr[%d] = 0;\n' % i for i in range(5))
f.close()

with open('foo.js') as f:
    print f.readline()
    print f.readlines(2)
    print f.read()
