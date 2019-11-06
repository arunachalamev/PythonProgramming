# Given a list of non-negative numbers and a target integer k, 
# write a function to check if the array has a continuous subarray of size at least 2 
# that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

def checkSubarraySum(nums,k):

    if k == 0:
        return any(nums[i] == 0 and nums[i + 1] == 0 for i in range(len(nums) - 1))
    mods, cum_sum_mod_k = {0: -1}, 0
    for i, n in enumerate(nums):
        cum_sum_mod_k = (cum_sum_mod_k + n) % k
        if cum_sum_mod_k in mods and i - mods[cum_sum_mod_k] > 1:
            return True
        if cum_sum_mod_k not in mods:
            mods[cum_sum_mod_k] = i
    return False


print(checkSubarraySum([23, 2, 4, 6, 7],6))
# True Because [2, 4] is a continuous subarray of size 2 and sums up to 6.


print(checkSubarraySum([23, 2, 6, 4, 7],6))
# True Because [2, 6, 4] is an continuous subarray of size 3 and sums up to 12.


# TestCase
# [0,0],0 - True
# [0],0   - False

