#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp_sum = 0
        max_sum = 0
        
        for i in range(len(nums)):
            temp_sum = max(nums[i], temp_sum + nums[i])
            max_sum = max(max_sum , temp_sum)
        return max_sum

