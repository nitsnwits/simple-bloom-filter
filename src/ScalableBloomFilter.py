#!/usr/bin/env python

#
# Simple implementation of Scalable bloom fitler in python
#
#

from bloomFilter import BloomFilter


class ScalableBloomFilter(BloomFilter):
	"""
	Inherits BloomFilter, creates Bloom Filters in Geometric Progression
	as and when capacity of a Bloom Filter is reached
	"""
	DEFAULT_GROWTH_RATE = 2;
	FAST_GROWTH_RATE = 4;
	DEFAULT_FP_CHANCE = 0.01;
	DEFAULT_CAPACITY = 100;
	def __init__(self, initialCapcity = DEFAULT_CAPACITY, growthRate = DEFAULT_GROWTH_RATE, falsePositiveProbability = DEFAULT_FP_CHANCE):
		self.bloomFiltersArray = []
		self.growthRate = growthRate
		self.initialCapcity = initialCapcity
		self.falsePositiveProbability = falsePositiveProbability
		self._setup()

	def _setup(self):
		"""
		Setup and create first bloom filter here
		Add this filter to bloomFiltersArray
		Calculations would always use last element of bloomFiltersArray
		"""

	def add(self, key):
		"""
		Lazy instantiation of self.bloomFiltersArray
		"""
		if not self.bloomFiltersArray:
			bf = BloomFilter(self.initialCapcity, 2) #TODO: Calculate k on runtime here
			self.bloomFiltersArray.append(bf)
		else:
			bf = self.bloomFiltersArray[-1]
			if bf.length() >= self.initialCapcity:
				bf = BloomFilter(self.initialCapcity * self.growthRate, 2) # TODO: Calculate k on runtime, when fp_chance is multiplied by growth rate (0.9)
				self.bloomFiltersArray.append(bf)
		bf.add(key) # This will use the super class add method

	def contains(self, key):
		for f in reversed(self.bloomFiltersArray):
			if f.contains(key):
				return True
		return False

	def clear(self):
		"""
		Clean up itself, call super method for each filter in the array
		"""
		for f in self.bloomFiltersArray:
			f.clear()

	def generateStats(self):
		"""
		generate status about how many filters have been created nd super
		"""
		print "Number of filters created: ", len(self.bloomFiltersArray)
		for f in self.bloomFiltersArray:
			f.generateStats()

	def length(self):
		return len(self.bloomFiltersArray)