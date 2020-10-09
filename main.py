import boto3
from my_subdir.functions import function_subdir
#from my_subdir import functions


print('im outside')

def hello_world():
	print("hello world!")
	function_subdir()
	#functions.function_subdir()


if __name__=='__main__':
	hello_world()