

class Solution:
    # can we sum to target with given arr
    # returns Boolean
    def canSum(self, target, arr, memo={}):
        if target in memo:
            return memo[target]
        if target == 0:
            return True
        if target < 0:
            return False
        
        for num in arr:
            if self.canSum(target - num, arr, memo):
                memo[target] = True
                return memo[target]
        
        memo[target] = False
        return False
    # m = target 
    # n = array
    # T: O(n*m)
    # S: O(m)

    # how to sum to target, given arr
    def howSum(self, target, arr, memo={}):
        if target == 0:
            return []
        if target < 0:
            return None
        if target in memo:
            return memo[target]
        
        for num in arr:
            res = self.howSum(target - num, arr, memo)
            if res != None:
                memo[target] = res + [num]
                return res + [num]

        memo[target] = None
        return None

    # m = target 
    # n = array
    # T: O(n*m^2)
    # S: O(m)

    # return the smallest best array that sums up to the target
    def bestSum(self, target, arr, memo={}):
        if target == 0:
            return []
        if target < 0:
            return None
        if target in memo:
            return memo[target]
        shortest_combination = None

        for num in arr:
            res = self.bestSum(target - num, arr, memo)
            if res != None:
                combination = res + [num]
                if (shortest_combination == None or (len(shortest_combination) > len(combination))):
                    shortest_combination = combination
                    memo[target] = combination

        memo[target] = shortest_combination
        return shortest_combination
    
    # T: O(n * m^2)
    # S: O(m)

s = Solution()
# canSum
# print(s.canSum(7, [2, 4], {}))       # False
# print(s.canSum(7, [5, 3, 4, 7], {})) # True
# print(s.canSum(300, [7, 14], {}))    # False


#howSum
# print(s.howSum(7, [2, 3], {}))       # [3, 2, 2]
# print(s.howSum(7, [5, 3, 4, 7], {})) # [4, 3]
# print(s.howSum(300, [7, 14], {}))    # None

#bestSum
# print(s.bestSum(7, [5, 3, 4, 7])) # [7]
# print(s.bestSum(8, [2, 3, 5])) # [3, 5]
# print(s.bestSum(100, [1, 2, 5, 25])) # [25, 25, 25, 25]


