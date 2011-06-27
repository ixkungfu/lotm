import re

re_string = '{{(.*?)}}'

some_string = 'this is a string with {{words}} embedded in {{curly brackets}} \
        to show an {{example}} of {{regular expressions}}'

# uncompile
for match in re.findall(re_string, some_string):
    print 'MATCH->', match

# compile
re_obj = re.compile('{{(.*?)}}')
for match in re_obj.findall(some_string):
    print 'MATCH->', match

re_obj = re.compile(r'\bt.*?e\b')
print re_obj.findall('time tame tune tint tire')

re_obj = re.compile('\bt.*?e\b')
print re_obj.findall('time tame tune tint tire')
