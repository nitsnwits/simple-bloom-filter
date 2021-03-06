simple-bloom-filter
===================

#### Implementation Details
**BloomFilter.py**: A simple bloom filter implementation in Python. This Bloom Filter uses murmurhash and python's own hash function to implement k hashing of BloomFilter. Before creating the filter, m and k need to be provided. A scalable bloom filter implementation is in progress.

**CountingBloomFilter.py**:Added a Counting Bloom Filter implementation using Lists. This Bloom Filter supports deletion of a key and inherits other properties from Bloom Filter.

**ScalableBloomFilter.py**: Added a naive implementation of Scalable Bloom Filters. SBF, when tested with a capacity of 10 bits and 1000 elements to be inserted, creates more instances of simple Bloom Filter and scales as per requirements. Inherits other properties from Bloom Filter.

#### Unit Tests and Load Tests
**testBloomFilter.py**: Unit Test and Load Tests for Bloom Filter
**testCountingBloomFilter.py**: Unit Test and Load Tests for Counting Bloom Filter
**testScalableBloomFilter.py**: Unit Test and Load Tests for Scalable Bloom Filter

#### How to run tests
- To setup : `pip install -r requirements.txt`
- To test Bloom Filter : `./testBloomFilter.py`
- To test Counting Bloom Filter: `./testCountingBloomFilter.py`
- To test Scalable Bloom Filter: `./testScalableBloomFilter.py`

#### Show me the runs

**Bloom Filter Tests**
```
~/simple-bloom-filter 663: -> ./testBloomFilter.py 

Testing BloomFilter implementation:

Test: OK 	Key: 'database' is present
Test: OK 	Key: 'cassandra' is present
Test: OK Random Key not present

Unit Test Completed


Load test BloomFilter implementation:

Added  200000  keys to BloomFilter
Current length of BF: 200000
Load test OK. All existent keys are present
Number of false positives: 10789
Actual False positive rate:  10.789
Probability of false positives:  0.108688872046
Predicted false positive rate:  10.8688872046
Number of elements entered in filter:  200000.0
Number of bits in filter:  1000000.0
Number of hashes in filter:  2.0

Load test Completed

~/simple-bloom-filter 664: ->
```

**Counting Bloom Filter Tests**
```
~/simple-bloom-filter 664: -> ./testCountingBloomFilter.py 

Testing CountingBloomFilter implementation:

Test: OK 	Key: 'database' is not present
Test: OK 	Key: 'cassandra' is present
Test: OK Random Key not present
Probability of false positives:  0.00153746808199
Predicted false positive rate:  0.153746808199
Number of elements entered in filter:  2.0
Number of bits in filter:  100.0
Number of hashes in filter:  2.0

Unit Test Completed

~/simple-bloom-filter 665: ->
```

**Scalable Bloom Filter Tests**
```
~/simple-bloom-filter 665: -> ./testScalableBloomFilter.py 

Testing Scalable BloomFilter implementation:

Test: OK 	Key: 'database' is present
Test: OK 	Key: 'cassandra' is present
Test: OK Random Key not present

Unit Test Completed

Number of filters created:  1
Probability of false positives:  0.00339136954866
Predicted false positive rate:  0.339136954866
Number of elements entered in filter:  3.0
Number of bits in filter:  100.0
Number of hashes in filter:  2.0

Load test ScalableBloomFilter implementation:

Added  1000  keys to BloomFilter
Current length of BF: 10
Load test OK. All existent keys are present
Number of false positives: 99860
Actual False positive rate:  99.86
Number of filters created:  10
Probability of false positives:  0.747645072416
Predicted false positive rate:  74.7645072416
Number of elements entered in filter:  100.0
Number of bits in filter:  100.0
Number of hashes in filter:  2.0
Probability of false positives:  0.399576400894
Predicted false positive rate:  39.9576400894
Number of elements entered in filter:  100.0
Number of bits in filter:  200.0
Number of hashes in filter:  2.0
[ output truncated ]

Load test Completed

~/simple-bloom-filter 666: ->
```
