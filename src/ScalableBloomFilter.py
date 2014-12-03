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
	DEFAULT_FP_CHANCE = 0.001;
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