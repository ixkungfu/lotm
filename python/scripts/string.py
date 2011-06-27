#!/usr/bin/env python
import subprocess

res = subprocess.Popen(['uname', '-sv'], stdout=subprocess.PIPE)
uname = res.stdout.read().strip()

print uname

# in, not in
print "Linux in uname: %s" % ('Linux' in uname)
print "Linux not in uname: %s" % ('Linux' not in uname)

# index, find
print "uname.find('Linux'): %s" % (uname.find('Linux'))
print "uname.find('Unix'): %s" % (uname.find('Unix'))
print "uname.index('Linux'): %s" % (uname.index('Linux'))
#print "uname.index('Unix'): %s" % (uname.index('Unix'))

# scale string
smp_index = uname.index('SMP')
print 'uname.index("SMP"): %s' % (uname.index('SMP'))
print 'uname[smp_index:]:'
print uname[smp_index:]
print 'uname[:smp_index]:'
print uname[:smp_index]
print uname

# startswith, endswith
some_string = 'Raymond Luxury-Yacht'
print 'some_string.startswith("Raymond"): %s' % (some_string.startswith('Raymond'))
print 'some_string.startswith("Throatwarbler"): %s' % (some_string.startswith('Throatwarbler'))
print 'some_string.endswith("Luxury-Yacht"): %s' % (some_string.endswith('Luxury-Yacht'))
print 'some_string.endswith("Raymond"): %s' % (some_string.endswith('Throatwarbler'))

# lstrip, rstrip, strip
whitespaces = '\n\t Kiss It Simple & Stupid!\n \t\r'
print whitespaces.lstrip()
print whitespaces.rstrip()
print whitespaces.strip()

xml_tag = '<some_tag>'
print xml_tag.lstrip('<')
print xml_tag.rstrip('>')
print xml_tag.strip('><')

foo_str = '<fooooo>blah<foo>'
print foo_str.strip('><fo')
print foo_str.strip('<fo>')

# upper, lower
mixed_case_string = 'VOrpal BUnny'
print mixed_case_string == 'vorpal bunny'
print mixed_case_string.lower() == 'vorpal bunny'
print mixed_case_string == 'VORPAL BUNNY'
print mixed_case_string.upper() == 'VORPAL BUNNY'

# split
pipe_delim_string = 'pipepos1|pipepos2|pepepos3'
print pipe_delim_string.split('|')
two_field_string = '8901876, This is a freeform, plain text, string'
print two_field_string.split(',', 1)
prosaic_string = 'Insert your clever litte piece of text here.'
print prosaic_string.split()

# splitlines
multiline_string = '''This
is
a multiline
piece of
text'''
print multiline_string.split()
print multiline_string.splitlines()

# join
some_list = ['one', 'two', 'three', 'four']
print ','.join(some_list)
some_list = [0, 1, 2, 3]
#print ','.join(some_list) # throww TypeError
print ','.join([str(i) for i in some_list])

# replace
replacable_string = 'tran nation hibernational'
print replacable_string.replace('nation', 'natty')

# unicode
unicode_string = u'this is a unicode string'
print unicode_string
print unicode('this is a unicode string')
