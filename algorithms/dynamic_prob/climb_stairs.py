'''
Climbing Stairs (https://leetcode.com/problems/climbing-stairs/)
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
total = 0
d = set()

def climbStairs(n):
	global total
	if n == 0:
		total += 1
	else:
		if n >= 1:
			climbStairs(n - 1)
		if n >= 2:
			climbStairs(n - 2)
	return total

print(climbStairs(4))

# def iterClimbStairs(n):
# 	steps = 0
# 	while:
# 		for i in (1,2):

total = 0

class Solution(object):
	def climbStairs(self, n):
		"""
        :type n: int
        :rtype: int
        """
		global total
		if n == 0:
			total += 1
		else:
			if n >= 1:
				self.climbStairs(n - 1)
			if n >= 2:
				self.climbStairs(n - 2)
		return total

s = Solution()
print(s.climbStairs(3))
