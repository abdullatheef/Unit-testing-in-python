import oddeven
import unittest

class KnownValues(unittest.TestCase):
	knownValues=((1,'odd'),
				 (2,'even'),
                 (11,'odd'))
	def testoddeven(self):
		for i,j in self.knownValues:
			result=oddeven.testoe(i)
			self.assertEqual(j,result)
class OddEvenBadInput(unittest.TestCase):
	def testZero(self):
		self.assertRaises(oddeven.ZeroError, oddeven.testoe,0)
	def testNonInteger(self):
		self.assertRaises(oddeven.NonIntegerError, oddeven.testoe,6.5)
	def testString(self):
		self.assertRaises(oddeven.StringError, oddeven.testoe,"abc")

if __name__ == "__main__":
    unittest.main() 
