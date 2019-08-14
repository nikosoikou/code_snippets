
"""
# Solution

- create a dict A that maps integers n to a boolean that tells if number is happy
- create a dict B that maps integers n to a set of derived
  integers from n that are not equal to 1
- if number n in A, return the value. if not, calculate sum of squares and get result
- if result is equal to 1, add number to A as true and return true
- if result is in B for the given n add result to A as false and return false
- if result not in B, add result to B and call the function with result as an argument
"""

happy_list = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139, 167, 176, 188, 190, 192, 193, 203, 208, 219, 226, 230, 236, 239,
              262, 263, 280, 291, 293, 301, 302, 310, 313, 319, 320, 326, 329, 331, 338, 356, 362, 365, 367, 368, 376, 379, 383, 386, 391, 392, 397, 404, 409, 440, 446, 464, 469, 478, 487, 490, 496]

from collections import defaultdict
# seen = set()


def is_happy(n):
    x = sum(int(i) ** 2 for i in str(n))
    if x == 1:
        return True
    if x in seen:
        return False
    seen.add(n)
    seen.add(x)
    return is_happy(x)


n = 100

for i in range(1, n + 1):
    seen = set()
    if is_happy(i):
        print(f'The number {i} is happy')
    else:
        print(f'The number {i} is not happy')
