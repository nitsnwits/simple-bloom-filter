#!/usr/bin/env python

#
# Simple implementation of bloom fitler in python
#
#

import sys
import mmh3 # murmurhash: is faster for blooms
import BitVector
import math

# set default encoding to utf-8
reload(sys)
sys.setdefaultencoding('utf-8')


class BloomFilter(object):
	"""
	Implement a simple bloom filter in python
	"""
	def __init__(self, m, k):
		# decide methods and how many and what hashes to be used
		self.m = m # number of bits in the array
		self.k = k # number of hashes to be used
		self.n = 0 # total count of the elemnts inserted in the set, intialized to zero, if this is incremented on add, this will be length of the filter, given elements are not removed
		self.bv = BitVector.BitVector(size = self.m)


	def getBitArrayIndices(self, key):
		"""
		hashes the key for k defined,
		returns the positions in the bit array for this key
		returns a list of integers as the indices positions
		"""
		returnList = []
		for i in range(1, self.k + 1):
			returnList.append((hash(key) + i * mmh3.hash(key)) % self.m)
		#print "Indices list for key: ", key, " is: ", str(returnList)
		return returnList

	def add(self, key):
		"""
		Insert an element to the filter, rest is application insert
		"""
		for i in self.getBitArrayIndices(key):
			self.bv[i] = 1
		# to check length
		self.n += 1

	def contains(self, key):
		"""
		returns boolean whether element exists in the set or not
		"""
		for i in self.getBitArrayIndices(key):
			if self.bv[i] != 1:
				return False
		return True

	def length(self):
		"""
		Returns the current size of Bloom filter
		"""
		return self.n

	def getStats(self):
		"""
		Calculates and returns the statistics of a filter
		Probability of FP, n, m, k, predicted false positive rate.
		"""
		n = self.n
		m = self.m
		k = self.k
		p_fp = math.pow(1.0 - math.exp(-(k*n)/m), k)
		print "Probability of false positives: ", p_fp
		print "Predicted false positive rate: ", p_fp * 100.0
		print "Number of elements entered in filter: ", n
		print "Number of bits in filter: ", m
		print "Number of hashes in filter: ", k

	def clear(self):
		"""
		Reinitizes the filter and clears old values and statistics
		"""
		self.n = 0
		self.bv = BitVector.BitVector(size = self.m)
