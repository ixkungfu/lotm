import urllib

url_file = urllib.urlopen('http://docs.python.org/lib/module-urllib.html')

urllib_docs = url_file.read()

print urllib_docs

url_file.close()

print len(urllib_docs)

print urllib_docs[:80]

print urllib_docs[-80:]
