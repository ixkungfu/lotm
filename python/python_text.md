priPython Text
===========

## String
### 单、双引号、三引号、转移
    >> s = "This is a string 'quotes' in it"
    >> s
    >> s = 'This is a string \'quotes\' in it'
    >> s
    >> s = 'This is a string "quotes" in it'
    >> s
    >> s = '''this is a
    ... multiline string'''
    >> s

### str
1. in, not in
2. find(), index()
3. startswith(), endswith()
4. lstrip(), rstrip(), strip()
5. upper(), lower()
6. split()
7. splitlines()
8. join()
9. replace()
10. Unicode
    unicode()
    http://docs.python.org/howto/unicode
11. re: use compile, better performance
    findall(), finditer(), match(), search()
12. file
    open(filename, pattern, cachesize)
        pattern: r(read, default), w(write), a(additional), b(biarry)
    f.read(), f.readline(), f.readlines(), f.write(), f.writelines(), f.close()
13. sys.stdin, sys.stdout 类似文件对象
    sys.stdin 标注输入，一个可读的文件对象
    sys.stdout 标准输出，一个可写的文件对象
14. StringIO
    可以让操作文本字符串像操作文件一样
15. urllib
16. unittest
17. ElementTree
