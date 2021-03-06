# Problem 012

## [Highly divisible triangular number](https://projecteuler.net/problem=12)

[<prev](./../DIR011_largest_product_in_a_grid/README.md)/[next>](./../DIR013_large_sum/README.md) 

### The example:
`The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:`
```
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
```
`Let us list the factors of the first seven triangle numbers:`
|||
|:---:|:---|
|**1:**|1|
|**3:**|1,3|
|**6:**|1,2,3,6|
|**10:**|1,2,5,10|
|**15:**|1,3,5,15|
|**21:**|1,3,7,21|
|**28:**|1,2,4,7,14,28|

`We can see that 28 is the first triangle number to have over five divisors.`


### The challenge:
`What is the value of the first triangle number to have over five hundred divisors?`

### Initial thoughts:
This is another challenge based around finding factors, so there will be some similarity to the previous prime-number based challenges. The difference here is that we need to find all the factors, not just to check if there are any at all.\
As explained before, 
[here](./../DIR003_largest_prime_factor/README.md#L20),
a good place to start is the `sqrt` of the number in question. Any factors lower will have a "partner" higher, and here we must also remember to include the number itself & 1 when counting factors.\
The other side to this problem is identifying triangular numbers. This should be fairly straightforward using a simple formula based on addition.

### Pseudocode for first iteration:
```
To find the next triangular number
----------------------------------
RECEIVE a list (of numbers)
  IF the list is empty
  THEN insert 0*
  ELSE 
    CALCULATE the last digit in the list + the amount of numbers in the list
    APPEND this new number to the list
RETURN the list of triangular numbers.
```
*NB while 0 is not considered a triangular number, its presence here helps the propogation of the list without affecting the outcome.
```
To count the factors
--------------------
SET the number of factors = 0
RECEIVE a number
CALCULATE the sqrt of the sqrt of the number
IF the sqrt is an integer
THEN increment the number of factors
ELSE do nothing

FOR every integer less than the sqrt (inc 1, not inc 0)
  CHECK if the number can be evenly divided by this integer
  IF it can be evenly divided
  THEN this integer is a factor
    INCREMENT the number of factors TWICE
  ELSE do nothing
RETURN the number of factors
```
```
To solve the problem
(by piecing the two parts together)
--------------------
SET list of triangular numbers as an empty list
START loop
  APPEND the next triangular number
  CHECK if the last number in the list has over 500 factors
  IF it has more than 500
  THEN this is the solution
    RETURN the solution
  ELSE continue the loop
END loop
```

### Comments on first iteration:
By using the above set of functions and coding them in python, I was able to find the solution.

### Refactoring:
