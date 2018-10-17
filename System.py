# 与系统交互
import os
# Get system toe
print('Your system is' + (' Windows' if os.name == 'nt' else ' other system'))

# Get environ 'path'
env = os.environ
path = env['path']
print('path', path)
path_elements = path.split(';')
for item in path_elements:
	print(item)

# Using system commands
os.system('echo Hello World!')
for root, dirs, files in os.walk('F:\\python'):
	print('root=', root)
	print('dirs=', dirs)
	print('files=', files)