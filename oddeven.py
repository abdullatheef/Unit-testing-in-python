class ZeroError(Exception):pass
class NonIntegerError(Exception):pass
class StringError(Exception):pass

#num=raw_input("Enter no:\n")
def testoe(n):
	if type(n)==int:
		if n==0:raise ZeroError,"zero..."
		elif n%2==0:
			return "even"
		else:
			return "odd"
	elif type(n)==str:
		raise StringError,"string...!!!!"
	else: raise NonIntegerError,"Non int...."



'''
try:
	testoe(int(num))
except TypeError:
	print "type error..."
'''
