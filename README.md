# Python and the Collatz Conjecture
- https://en.wikipedia.org/wiki/Collatz_conjecture

## Functions:
- test_num(n)  #takes a positive integer and calculates the number of steps to converge to 1

- test_range(init, final)  #calculates convergance for a range of positive integers

-  test_range_dict(init, final)    #calculates convergance for a range of positive integers using an optimized routine which utilizes previously found values in the range.

## Example usages in ipython3:
- %run collatz.py
- test_num(1152921504606846976)   #this is 2^60
- test_range(1,10000)
- test_range_dict(1, 10000)
 
## Timing
-   from timeit import Timer
-   t1 = Timer(lambda: test_range(1,100000))
-   t2 = Timer(lambda: test_range_dict(1,100000))
-   print t1.timeit(number=1)
-   print t2.timeit(number=1)
