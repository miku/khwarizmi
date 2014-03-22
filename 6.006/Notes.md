Lecture 2
=========

What is an algorithm?
---------------------

* computational procedure for solving a problem
* input -> algorithm -> output

* program vs algorithm (language vs pseudocode, formal reasoning)
* computer vs model of computation

Models of computation
---------------------

* what operations are available to algorithms and how much they cost

*Random access machine* (RAM). Has a memory. Words. In constant time an algorithm
can

* load O(1) words
* do O(1) computations
* store O(1) words

O(1) registers, hanging around. 

*Pointer machine* (corresponds to OO). With dynamically allocated objects. An
object has O(1) number of fields. A field is a word or a *pointer*. Points to
another object or is null, nil, None. Can follow pointers, but no pointer arithmetic.

Python model
------------

* has lists (RAM)
* has references (pointer machine)

But not just load and store.

1. lists (which are really arrays), O(1) time access
2. objects with O(1) attributes

Python lists use table doubling. Append is almost O(1) time.

	L1 + L2, O(1 + |L1| + |L2|)

	len(L), O(1)!
	x in L, O(n)


Sorting a list.

	L.sort() # O(n * log n * O(comparison))

Hashes (8-10):

	D[key] = value # O(1)

Addition, long:

	x + y, O(|x| + |y|)
	x * y, O((|x| + |y|)^(lg 3))

heapq.


Document distance problem
-------------------------

d(D1, D2)

Motivation. 

A document is a sequence of words. A word is a string of alphanumeric
characters. Maybe they are similar, if they have a lot of words in common.

A document is a vector.

	D[w] = 1 # number of times words w appears in document D.

Suggestions: Inner product (dot product).

	d'(D1, D2) = D1 * D2 = \Sum_w D1[w] * D2[w]

Measure of commonality. Higher dot product, more overlaps, shared words.
Problem with long documents. They look very similar. Not quite scale-invariant.

But, you could divide by the length of the vectors. 

	d'(D1, D2) = (D1 D2) / (|D1| |D2|)

Looks familiar? arccos. 0 angle, identical. 90 different.

Algorithm:

* split a document into word
* compute word frequencies (doc vectors)
* compute the dot product

Implementation of cosine similarity (1M docs):

* 228.1s
* 164s
* 123s
* 71s
* 18.3s
* 11.5s
* 1.8s
* 0.2s

Split a document into words in python. Iterate through the words, gather them
in a dictionary. dict O(1) whp. Or O(|word|). So the sum of words (was the 71s version).


Lecture 3
---------

Two kinds of sorting, insertion and merge. Recurrences, and how to solve them.

All kind of natural use cases. Also, problems become easier, once items are
sorted, e.g. finding the median - which becomes O(1).

Also: BINARY SEARCH. Looking for a specific number or item. Linear, scan vs.
logarithmic time.

Or non-obvious inputs. 

Advantage of insertion sort over merge sort. In merge sort you need Theta(n)
auxiliary space. Whereas insertion sort need Theta(1), swap variables.

In-place merge sort possible, but with performance tradeoffs.

Recurrence tree can have different loads on different levels.

* equally distributed
* most work in root
* most work in leaves

