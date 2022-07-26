def twoSum(nums, target):
        mapping = {}
        
        for i in range(len(nums)):
            if target - nums[i] in mapping:
                print([mapping.get(target-nums[i]), i])
                return [mapping.get(target-nums[i]), i]
            else:
                mapping[nums[i]] = i
nums = [2, 7, 9 , 11]
# twoSum(nums, 9)
#====================================================================

# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
def find_averages_of_subarrays(K, arr):
    res = []
    start = 0
    windowSum = 0
    for end in range(len(arr)):
        windowSum += arr[end]
        if end >= K - 1:
            res.append(windowSum/K)
            windowSum -= arr[end]
            start += 1
    return res

# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].
def max_sub_array_of_size_k(k, arr):
    winSum = maxSum = 0
    start = 0
    for end in range(len(nums)):
        winSum += nums[end]
        if end >= k - 1:
            maxSum = max(maxSum, winSum)
            winSum -= nums[start]
            start += 1
    return maxSum

#====================================================================

# array [-1, 0, 2, 3], 3
# array [-1, 4, 2, 1, 3], 5

arr = [-1, 4, 2, 1, 3]
def tripletWithSmallerSum(arr, target):
    arr = sorted(arr)
    count = 0
    for i in range(len(arr) - 2):
        count += helperSum(arr, target-arr[i], i)
    return count

def helperSum(arr, target, i):
    count = 0
    start = i + 1
    end = len(arr) - 1
    while start < end:
        if arr[start] + arr[end] < target:
            count += end - start
            start += 1
        else:
            end -= 1
    return count

    

# print(tripletWithSmallerSum(arr, 5))


# tripletWithSmallerSum ([-1, 0, 2, 3], 3)//2, There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
# tripletWithSmallerSum ([-1, 4, 2, 1, 3], 5)//4, There are four triplets whose sum is less than the target: [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
# tripletWithSmallerSum ([-2,0,1,3], 2)//2, Because there are two triplets which sums are less than 2: [-2,0,1], [-2,0,3]
# tripletWithSmallerSum ([], 0)//0
# tripletWithSmallerSum ([0], 0)//0

def tripletWithSmallerTestRun(arr, target):
    count = 0
    arr = sorted(arr)
    for i in range(len(arr)-2):
        count += helper(arr, target-arr[i], i + 1)
    return count

def helper(arr, target, start):
    count = 0
    end = len(arr) - 1
    while start < end:
        curr = arr[end] + arr[start]
        if curr < target:
           count += end - start
           start += 1
        else:
            end -= 1
    return count
        


# print(tripletWithSmallerTestRun([-1, 4, 2, 1, 3], 5))
#====================================================================

# canAttendAllAppointments([[1,4], [2,5], [7,9]])
# //false, Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
# canAttendAllAppointments([[6,7], [2,4], [8,12]])
# //true, None of the appointments overlap, therefore a person can attend all of them.

# canAttendAllAppointments([[4,5], [2,3], [3,6]])
# //false, Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.

def canAttendAllAppointments(appointmentTimes):
    appointmentTimes.sort(key=lambda i:i[0])
    for i in range(len(appointmentTimes)-1):
        curr = appointmentTimes[i]
        nextCurr = appointmentTimes[i+1]
        if curr[1] > nextCurr[0]:
            return False
    return True

# print(canAttendAllAppointments([[4,5], [2,3], [3,6]]))
# print(canAttendAllAppointments([[6,7], [2,4], [8,12]]))

#====================================================================
# Min meeting rooms

def minMeetingRooms(meetings):
    if not meetings:
      return None
    if len(meetings) == 1:
      return len(meetings)
    
    meetings.sort(key=lambda i: i[0])
    rooms = [meetings[0]]
    i = 1
    while i < len(meetings):
      earlyRoom = getEarlyRoom(rooms)
      currentTime = meetings[i]
      print(earlyRoom, currentTime)
      if earlyRoom[1] <= currentTime[0]:
        # changes the value of the early room -- pass by value
        earlyRoom[1] = currentTime[1]
      else:
        rooms.append(currentTime)
      i += 1 
    return len(rooms)

def getEarlyRoom(rooms):
    rooms.sort(key=lambda i:i[1])
    return rooms[0]
    
# print(minMeetingRooms([[4,5], [2,3], [2,4], [3,5]])) # 2
# We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].

# minMeetingRooms([[1,4], [2,3], [3,6]])//2
# Since [1,4] overlaps with the other two meetings [2,3] and [3,6], we need two rooms to hold all the meetings.

# minMeetingRooms([[6,7], [2,4], [8,12]])//1 
# None of the meetings overlap, therefore we only need one room to hold all meetings.


# ===================================================
# Cyclic Sort
#===================================================

# def cyclicSort(nums):
    

# print(cyclicSort ([3, 1, 5, 4, 2]))
# cyclicSort ([2, 6, 4, 3, 1, 5])
# cyclicSort ([1, 5, 6, 4, 3, 2])


# ===================================================
#  Find the Corrupt Pair
#===================================================

def findCorruptNumbers(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    print(nums)
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return [nums[i], i + 1]
    return [-1, -1]

# print(findCorruptNumbers([3, 1, 2, 5, 2]))
# findCorruptNumbers([3, 1, 2, 5, 2])//[2, 4], '2' is duplicated and '4' is missing.
# findCorruptNumbers([3, 1, 2, 3, 6, 4])// [3, 5], '3' is duplicated and '5' is missing.


# ===================================================
# Reverse alternate K nodes in a Singly Linked List
#===================================================


# k nodes in a linked list
import math
 
# Link list node
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()

def reverse_alternate_k_elements(head, k):
    if not head and k < 1:
        return head
    curr, prev = head, None
    while True:
        last_node_of_previous_part = prev
        last_node_of_sub_list = curr
        
        i = 0
        while curr is not None and i < k: 
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
            i += 1

        if last_node_of_previous_part is not None:
            last_node_of_previous_part.next = prev
        else:
            head = prev

        last_node_of_sub_list.next = curr

        if curr is None:
            break

        i = 0
        while curr is not None and i < k: 
            prev = curr
            curr = curr.next
            i += 1

        if curr is None:
            break

    return head

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_alternate_k_elements(head, 2)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


# main()


# ===================================================
#  Find the Corrupt Pair
#===================================================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
def findSuccessor(root, num):
    if not root:
        return None
    q = collections.deque()
    q.append(root)
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node:
                if node.val == num:
                    if node.left:
                        return node.left.val
                    if node.right:
                        return node.right.val
                else:
                    q.append(node.left)
                    q.append(node.right)
    return None
    

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
result = findSuccessor(root, 1)
if (result != None):
  print(result)
