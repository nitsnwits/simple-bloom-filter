#!/usr/bin/env python

#
# Test the bloom filter imlementation
# TODO: Benchmark False Positives, test run time,
# TODO: Compare murmurhash, sha, python hash, cityhash, pyfasthash?
#

from src.bloomFilter import BloomFilter
import uuid

def getRandomString():
	return str(uuid.uuid4())


def unitTestBloomFilter():
	"""
	Create once instance of BloomFilter and test few keys lookup
	"""
	print "\nTesting BloomFilter implementation:\n"
	bf = BloomFilter(100, 2)
	bf.add('neeraj')
	bf.add('database')
	bf.add('cassandra')

	# test the keys if present
	if bf.contains('database'):
		print "Test: OK \tKey: 'database' is present"
	else:
		print "Test: Failed \tKey: 'database' is not present"
	if bf.contains('cassandra'):
		print "Test: OK \tKey: 'cassandra' is present"
	else:
		print "Test: Failed \tKey: 'cassandra' is not present"
	if bf.contains('anykey'):
		print "Test: Failed Random Key present"
	else:
		print "Test: OK Random Key not present"
	print "\nUnit Test Completed\n"

def loadTestBloomFilter(n, m, k):
	"""
	Create n keys in BF of size m
	Store 100 keys for retreival, retrieve them
	Hit 100 random non-existent keys, see how many false positives are received
	"""
	print "\nLoad test BloomFilter implementation:\n"
	existentKeys = []

	# Create a bigger Bloom Filter
	bf = BloomFilter(m, k)
	for i in range(0, n):
		randomString = getRandomString()
		bf.add(randomString)
		if (i % 1000) == 0:
			existentKeys.append(randomString)		

	print "Added ", n, " keys to BloomFilter"
	print "Current length of BF: " + str(bf.length())

	# Check existent keys
	for i in existentKeys:
		if not bf.contains(i):
			print "Load test failed. Existent key not present"
	print "Load test OK. All existent keys are present"

	# Check non-existent keys
	fp = 0
	fpCheckCount = 100000
	for i in range(0, fpCheckCount):
		if bf.contains(getRandomString()):
			fp += 1

	print "Number of false positives: " + str(fp)
	print "Actual False positive rate: ", 100.0 * float(fp)/float(fpCheckCount)
	bf.generateStats()

	print "\nLoad test Completed\n"


if __name__ == '__main__':
	unitTestBloomFilter()
	# filter of 1 Mb, 1 million bits, 20% elements entered, k=2
	loadTestBloomFilter(200000, 1000000, 2)

