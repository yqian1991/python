import bisect


class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0

        f = [nums[0]]
        for i in xrange(1, len(nums)):
            if nums[i] > f[-1]:
                f.append(nums[i])
                print 'f:', f
            else:
                pos = bisect.bisect_left(f, nums[i])
                print pos
                f[pos] = nums[i]
                print 'f:', f
        return len(f)

sol = Solution()
nums = [1, 3, 6, 2]
print sol.lengthOfLIS(nums)
