import boto3
from my_package.my_module import my_function
#from my_package import my_module


print('im outside')

def hello_world():
	print("hello world!")
	my_function()
	#my_module.my_function()


if __name__=='__main__':
	hello_world()