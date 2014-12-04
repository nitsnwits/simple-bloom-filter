simple-bloom-filter
===================

##### Implementation Details
*BloomFilter.py*: A simple bloom filter implementation in Python. This Bloom Filter uses murmurhash and python's own hash function to implement k hashing of BloomFilter. Before creating the filter, m and k need to be provided. A scalable bloom filter implementation is in progress.

*CountingBloomFilter.py*:Added a Counting Bloom Filter implementation using Lists. This Bloom Filter supports deletion of a key and inherits other properties from Bloom Filter.

*ScalableBloomFilter.py*: Added a naive implementation of Scalable Bloom Filters. SBF, when tested with a capacity of 10 bits and 1000 elements to be inserted, creates more instances of simple Bloom Filter and scales as per requirements. Inherits other properties from Bloom Filter.

##### Unit Tests and Load Tests
*testBloomFilter.py*: Unit Test and Load Tests for Bloom Filter
*testCountingBloomFilter.py*: Unit Test and Load Tests for Counting Bloom Filter
*testScalableBloomFilter.py*: Unit Test and Load Tests for Scalable Bloom Filter

##### How to run tests
To setup : `pip install -r requirements.txt`

To test Bloom Filter : `./testBloomFilter.py`

To test Counting Bloom Filter: `./testCountingBloomFilter.py`

To test Scalable Bloom Filter: `./testScalableBloomFilter.py`
