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
            if len(shorter) == len(longer):
                short_idx += 1
        else: #Characters are the same
            short_idx += 1
        long_idx += 1
    if difference:
        return False
    return True

# Hash table approach. O(n) time complexity and O(n) space complexity.
def one_away(s1, s2):
    if s1 == s2:
        return True
    length_diff = abs(len(s1)-len(s2))
    if length_diff > 1:
        return False
    unique_chars = defaultdict(lambda:0)
    for i in range(len(s1)):
        unique_chars[s1[i]]+= 1
    print unique_chars
    for j in range(len(s2)):
        if unique_chars[s2[j]] > 0:
            unique_chars[s2[j]] -= 1
    sum = 0
    for key in unique_chars:
        if unique_chars[key]:
            sum += unique_chars[key]
    print unique_chars
    print sum
    if sum > 1:
        return False
    return True
