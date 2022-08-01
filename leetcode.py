# 410. Split Array Largest Sum (HARD)


# Given an array nums which consists of non-negative integers and an integer m, 
# you can split the array into m non-empty continuous subarrays.

# Write an algorithm to minimize the largest sum among these m subarrays.

# Example 1:

# Input: nums = [7,2,5,10,8], m = 2
# Output: 18
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
# Example 2:

# Input: nums = [1,2,3,4,5], m = 2
# Output: 9
# Example 3:

# Input: nums = [1,4,4], m = 3
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 106
# 1 <= m <= min(50, nums.length)


# class Solution:
#     def splitArray(self, nums: List[int], m: int) -> int:
        
#         left, right = max(nums), sum(nums)
        
#         while left < right:
#             # how we know when to start a new sub array
#             mid = left + (right - left) // 2
            
#             # this is to keep track of our sum in nums 
#             curr = 0
            
#             # this is the subarray size
#             count = 1
            
#             # go thru nums
#             for n in nums:
#                 # if our number is smaller than our sub array, continue to add to 
#                 curr += n
#                 if curr > mid:
#                     curr = n
#                     count += 1
#             if count > m:
#                 left = mid + 1
                
#             else:
#                 right = mid
                
#         return left



# ==================================================

# 1011. Capacity To Ship Packages Within D Days

# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we 
# load the ship with packages on the conveyor belt (in the order given by weights). 
# We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages 
# on the conveyor belt being shipped within days days.


# Example 1:

# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10

# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
# Example 2:

# Input: weights = [3,2,2,4,1,4], days = 3
# Output: 6
# Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
# 1st day: 3, 2
# 2nd day: 2, 4
# 3rd day: 1, 4
# Example 3:

# Input: weights = [1,2,3,1,1], days = 4
# Output: 3
# Explanation:
# 1st day: 1
# 2nd day: 2
# 3rd day: 3
# 4th day: 1, 1
 

# Constraints:

# 1 <= days <= weights.length <= 5 * 104
# 1 <= weights[i] <= 500

#  def shipWithinDays(self, weights: List[int], days: int) -> int:
#         left, right = max(weights), sum(weights)
        
        
#         while left < right:
#             # capacity
#             mid = left + (right - left) // 2
            
#             curr_w = 0
#             ship_cap = 1
            
#             for weight in weights:
#                 curr_w += weight
#                 if curr_w > mid:
#                     ship_cap += 1
#                     curr_w = weight
                
            
#             if ship_cap > days:
#                 left = mid + 1
#             else:
#                 right = mid
#         return left
# ==================================================

# 36. Valid Sudoku

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be 
# validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner 
# being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         # add each number to a row set
#         # add each number to a col set
#         # add each number to a box set
#         ROWS, COLS = len(board), len(board[0])
        
#         rowSet = { i: set() for i in range(ROWS) }
#         colSet = { i: set() for i in range(COLS) }
#         boxSet = collections.defaultdict(set)
        
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if board[r][c] == ".":
#                     continue
                
#                 if (board[r][c] in rowSet[r] or
#                     board[r][c] in colSet[c] or
#                     board[r][c] in boxSet[r//3, c//3]):
#                     return False
                
#                 rowSet[r].add(board[r][c])
#                 colSet[c].add(board[r][c])
#                 boxSet[r//3, c//3].add(board[r][c])
#         return True
# ==================================================


# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that 
# answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# def productExceptSelf(self, nums: List[int]) -> List[int]:
# #         [1,2,3,4]
# #         left  = [1, 1, 2, 6]
# #         right = [24, 12, 4, 1]
        
# #         res =   [24, 12, 8, 6]
        
#         # prefix = [1, 1, 2, 6]
#         # nums =   [1, 2, 3, 4]
        
#         n = len(nums)
        
     
#         res = [0] * n
#         res[0] = 1
        
#         for i in range(1, n):
#             res[i] = res[i-1] * nums[i-1]
#         right = 1
#         for i in range(n-1, -1, -1):
#             res[i] = res[i] * right
#             right *= nums[i]
        
#         return res
# ==================================================

# 42. Trapping Rain Water

# Given n non-negative integers representing an elevation map where the 
# width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented 
# by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water 
# (blue section) are being trapped.

# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105
# Accepted
# 1,223,389

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         # do prefix and postfix -> get max of left/right
        
#         left, right = 0, len(height)-1
#         left_max = 0
#         right_max = 0
#         area = 0
    
#         while left < right:
#             if height[left] < height[right]:
#                 if height[left] > left_max:
#                     left_max = height[left]
#                 else:
#                     area += left_max - height[left]
#                 left += 1
#             else:
#                 if height[right] > right_max:
#                     right_max = height[right]
#                 else:
#                     area += right_max - height[right]
#                 right -= 1
        
#         return area
# ==================================================

# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
        
#         seen = set()
        
#         left = 0
#         longest = 0
        
#         for i in range(len(s)):
#             while s[i] in seen:
#                 seen.remove(s[left])
#                 left += 1
#             seen.add(s[i])
#             longest = max(longest, i - left + 1)
#         return longest
        
# ==================================================

# 239. Sliding Window Maximum
# You are given an array of integers nums, there is a sliding 
# window of size k which is moving from the very left of the 
# array to the very right. You can only see the k numbers in the 
# window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         q = collections.deque()
#         res = []
#         l = r = 0
#         while r < len(nums):
#             # pop smaller values from the left
#             while q and nums[q[-1]] < nums[r]:
#                 q.pop()
#             q.append(r)
            
#             # remove left val from window
#             if l > q[0]:
#                 q.popleft()
            
#             if r + 1 >= k:
#                 res.append(nums[q[0]])
#                 l += 1
#             r += 1         
            
#         return res
# ==================================================

# 269. Alien Dictionary
# There is a new alien language that uses the English alphabet. 
# However, the order among the letters is unknown to you.

# You are given a list of strings words from the alien language's 
# dictionary, where the strings in words are sorted lexicographically 
# by the rules of this new language.

# Return a string of the unique letters in the new alien language 
# sorted in lexicographically increasing order by the new language's 
# rules. If there is no solution, return "". If there are multiple solutions, return any of them.

# A string s is lexicographically smaller than a string t if at the 
# first letter where they differ, the letter in s comes before the
#  letter in t in the alien language. If the first min(s.length, t.length) letters 
# are the same, then s is smaller if and only if s.length < t.length.

 

# Example 1:

# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"
# Example 2:

# Input: words = ["z","x"]
# Output: "zx"
# Example 3:

# Input: words = ["z","x","z"]
# Output: ""
# Explanation: The order is invalid, so return "".
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of only lowercase English letters.

# class Solution:
#     def alienOrder(self, words: List[str]) -> str:
# #         ["wrt",
# #          "wrf",
# #          "er",
# #          "ett",
# #          "rftt"]
        
# #         w -> e -> r -> t -> f
#         adj = {char: set() for word in words for char in word}
        
#         for i in range(len(words) - 1):
#             w1, w2 = words[i], words[i + 1]
#             minLength = min(len(w1), len(w2))
#             if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]:
#                 return ""
#             # ape
#             # apps
#             for j in range(minLength):
#                 if w1[j] != w2[j]:
#                     adj[w1[j]].add(w2[j])
#                     break
#         visited = {}  # True: current path, False: we already visited
#         res = []
        
#         def dfs(char):
#             if char in visited:
#                 return visited[char]
            
#             visited[char] = True
            
#             for neighbor in adj[char]:
#                 if dfs(neighbor):
#                     return True
            
#             visited[char] = False
#             res.append(char)

#         for c in adj:
#             if dfs(c):
#                 return ""
#         print(res)
#         return "".join(reversed(res))