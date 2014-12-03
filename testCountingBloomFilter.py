#!/usr/bin/env python

#
# Test the counting bloom filter imlementation
#

#from src.bloomFilter import BloomFilter
from src.countingBloomFilter import CountingBloomFilter

import uuid

def getRandomString():
	return str(uuid.uuid4())


def unitTestCountingBloomFilter():
	"""
	Create once instance of BloomFilter and test few keys lookup
	"""
	print "\nTesting CountingBloomFilter implementation:\n"
	cbf = CountingBloomFilter(100, 2)
	cbf.add('neeraj')
	cbf.add('database')
	cbf.add('cassandra')
	cbf.add('cassandra')
	cbf.remove('cassandra')
	cbf.remove('database')

	# database should not be present, cassandra should be present

	# test the keys if present
	if not cbf.contains('database'):
		print "Test: OK \tKey: 'database' is not present"
	else:
		print "Test: Failed \tKey: 'database' is present"
	if cbf.contains('cassandra'):
		print "Test: OK \tKey: 'cassandra' is present"
	else:
		print "Test: Failed \tKey: 'cassandra' is not present"
	if cbf.contains('anykey'):
		print "Test: Failed Random Key present"
	else:
		print "Test: OK Random Key not present"
	cbf.generateStats()
	print "\nUnit Test Completed\n"
	cbf.clear()

if __name__ == '__main__':
	unitTestCountingBloomFilter()