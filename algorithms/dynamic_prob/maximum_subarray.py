'''
Maximum SubArray (https://leetcode.com/problems/maximum-subarray/)
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Breaking down problem:
	- Every time we check an element, we take the left part of the element in consideration because we expect contiguous array.
	                ↓
		[-2, 1, -3, 4, -1, 2, 1, -5, 4] => checking this element
	- If the sum of the left is negative, it's not helpful to add the left into array.
	- Once the left sum is negative, we ignore the left. So we need to keep track of the maximum sum value.
Implementation:
	1. Prepare a variable to update the max value
	2. Loop over the list:
	    - Calculate the current sum: if the current sum (left sum) is not negative, we add it to the current element
	    - Update the max value if the current sum is greater than the max value
'''

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxSum = 0
# Solution 1: recursive
class SubArray:
	maxSum = 0
	def maxSub(self, a, sum):
		if len(a) == 0:
			pass
		else:
			sum = a[0] if sum < 0 else sum + a[0]
			self.maxSub(a[1:], sum)
		if sum > self.maxSum:
			self.maxSum = sum
		return self.maxSum

# Solution 2: iteration
def iterMaxSub(a):
	maxCur = a[0]
	maxGlobal = a[0]
	for i in reversed(range(1,len(a))):
		maxCur = max(a[i], a[i] + maxCur)
		maxGlobal = max(maxCur, maxGlobal)
	print('result: ', maxGlobal)
# iterMaxSub(nums)
a = SubArray()
print(a.maxSub(nums, 0))