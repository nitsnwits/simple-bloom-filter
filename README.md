simple-bloom-filter
===================

*BloomFilter.py*: A simple bloom filter implementation in Python. This Bloom Filter uses murmurhash and python's own hash function to implement k hashing of BloomFilter. Before creating the filter, m and k need to be provided. A scalable bloom filter implementation is in progress.

*CountingBloomFilter.py*:Added a Counting Bloom Filter implementation using Lists. This Bloom Filter supports deletion of a key and inherits other properties from Bloom Filter.

*ScalableBloomFilter.py*: Work in progress.

To setup : `pip install -r requirements.txt`
To test Bloom Filter : `./testBloomFilter.py`
To test Counting Bloom Filter: `./testCountingBloomFilter.py`
