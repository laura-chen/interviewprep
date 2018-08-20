# Given two sorted integer arrays nums1 and nums2, modify nums1 with the sorted
# values. 

def merge(nums1, nums2):
    pointer1, pointer2 = 0, 0
    merged = []
    m, n = len(nums1), len(nums2)
    if m == 0:
        return nums2
    if n == 0:
        return nums1
    while pointer1 < m and pointer2 < n:
        if nums1[pointer1] <= nums2[pointer2]:
            merged.append(nums1[pointer1])
            pointer1 += 1
        else:
            merged.append(nums2[pointer2])
            pointer2 += 1
    if pointer1 == m:
        for i in range(pointer2, n):
            merged.append(nums2[i])
    else:
        for j in range(pointer1, m):
            merged.append(nums1[j])
    return merged
