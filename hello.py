'''
condition = 0
while condition <10:
	print(condition)
	condition = condition+1
'''

'''
a = range(10)
while a:
	print(a[-1])
	a = a[:len(a)-1]
'''

'''
example_list = [1,2,3,4,5,6,7,8,9]
for i in example_list:
	print(i)
'''

'''
for i in range(1,10,2):
	print(i)
'''

'''
tup = ('python',2.7,66)
for i in tup:
	print(i)
'''

'''
dic = {}
dic['lan'] = 'python'
dic['version'] = 2.7
dic['platform'] = 64
for key in dic:
	print(key,dic[key])	#key为乱序
'''

'''
s = set(['python','python2','python3','python'])
for item in s:
	print(item)
'''

'''
def test():
	print('function')
	a=1+2
	print(a)
test()
'''

'''
import sys

def test():
	args = sys.argv
	if len(args)==1:
		print('hello world!')
	elif len(args)==2:
		print('hello,%s!' % args[1])
	else:
		print('Too many arguments!')
test()
'''

