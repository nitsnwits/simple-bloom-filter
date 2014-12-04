#!/usr/bin/env python

#
# Test the bloom filter imlementation
# TODO: Benchmark False Positives, test run time,
# TODO: Compare murmurhash, sha, python hash, cityhash, pyfasthash?
#

from src.scalableBloomFilter import ScalableBloomFilter
import uuid

def getRandomString():
	return str(uuid.uuid4())


def unitTestScalableBloomFilter():
	"""
	Create once instance of Scalable BloomFilter and test few keys lookup
	"""
	print "\nTesting Scalable BloomFilter implementation:\n"
	sbf = ScalableBloomFilter()
	sbf.add('neeraj')
	sbf.add('database')
	sbf.add('cassandra')

	# test the keys if present
	if sbf.contains('database'):
		print "Test: OK \tKey: 'database' is present"
	else:
		print "Test: Failed \tKey: 'database' is not present"
	if sbf.contains('cassandra'):
		print "Test: OK \tKey: 'cassandra' is present"
	else:
		print "Test: Failed \tKey: 'cassandra' is not present"
	if sbf.contains('anykey'):
		print "Test: Failed Random Key present"
	else:
		print "Test: OK Random Key not present"
	#bf.generateStats()
	print "\nUnit Test Completed\n"
	sbf.generateStats()
	sbf.clear()

def loadTestScalableBloomFilter(n, m, k):
	"""
	Try to load SBF and see how many filters are created when capacity is filled up
	"""
	print "\nLoad test ScalableBloomFilter implementation:\n"
	existentKeys = []

	# Create a bigger Bloom Filter
	sbf = ScalableBloomFilter()
	for i in range(0, n):
		randomString = getRandomString()
		sbf.add(randomString)
		if (i % 1000) == 0:
			existentKeys.append(randomString)		

	print "Added ", n, " keys to BloomFilter"
	print "Current length of BF: " + str(sbf.length())

	# Check existent keys
	for i in existentKeys:
		if not sbf.contains(i):
			print "Load test failed. Existent key not present"
	print "Load test OK. All existent keys are present"

	# Check non-existent keys
	fp = 0
	fpCheckCount = 100000
	for i in range(0, fpCheckCount):
		if sbf.contains(getRandomString()):
			fp += 1

	print "Number of false positives: " + str(fp)
	print "Actual False positive rate: ", 100.0 * float(fp)/float(fpCheckCount)
	sbf.generateStats()
	sbf.clear()

	print "\nLoad test Completed\n"

if __name__ == '__main__':
	#unitTestScalableBloomFilter()
	loadTestScalableBloomFilter(1000, 10, 2)

