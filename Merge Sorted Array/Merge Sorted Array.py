
def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    j = 0
    i = 0
    num_inserted = 0
    while j<n:
        if nums1[i]>=nums2[j]:
            nums1.insert(i, nums2[j])
            j += 1
            num_inserted += 1
        elif i>=(m+num_inserted) and nums1[i] == 0:
            nums1[i] = nums2[j]
            j += 1
        i += 1

    del nums1[m+n:]

nums1 = [4,0,0,0,0,0]
m = 1
nums2 = [1,2,3,5,6]
n = 5
print(merge(nums1, m, nums2, n))