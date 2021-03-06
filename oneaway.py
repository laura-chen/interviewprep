# Given two strings, determine whether or not the the strings are either 1
# insert or replace away from being equal.

from collections import defaultdict

# Pointer approach. O(n) time complexity and O(1) space complexity.
def one_away_pointer(s1, s2):
    if s1 == s2:
        return True
    length_diff = abs(len(s1)-len(s2))
    if length_diff > 1:
        return False
    if len(s1) >= len(s2):
        longer, shorter = s1, s2
    elif len(s2) > len(s1):
        shorter, longer = s2, s1
    short_idx, long_idx = 0, 0
    difference = False
    print shorter, longer
    while short_idx < len(shorter) and long_idx < len(longer):
        if shorter[short_idx] != longer[long_idx]:
            if difference:
                return False
            difference = True
            if len(shorter) == len(longer): #Replace operation. If this wasn't the case, there would have to be an insert. 
                 short_idx += 1
        else: #Characters are the same
            short_idx += 1
        long_idx += 1
    if difference:
        return True
    return True

print one_away_pointer("pale","ple")
