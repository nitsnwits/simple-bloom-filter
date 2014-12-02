#!/usr/bin/env python

#
# Simple implementation of bloom fitler in python
#
#

import sys
import hashlib
import mmh3 # murmurhash: is faster for blooms
import bitarray
import BitVector

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
