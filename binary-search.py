# you can only run binary search if the array is sorted
# otherwise we will need to sort the array and then run 
# the algorithm

class BinarySearch:
  def search(self, arr, target):
    left, right = 0, (len(arr)-1)

    while left <= right:
      mid = left + (right-left)//2
      if target == arr[mid]:
        return mid
      if arr[mid] > target:
        right = mid - 1
      else:
        left = mid + 1
    return -1

arr = [1, 2, 4, 7, 8, 10, 23, 34, 45]
b = BinarySearch()

print(b.search(arr, 20))



# Binary search template (Leetcode)

def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = 0, len(array)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left