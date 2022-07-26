
class algorithm:
    def __init__(self, arr=[3.1, 2.5, 5.8, 7.4, 9.0, 5.2, 2.1]) -> None:
        self.arr = arr
    

    def partition(self, arr, low, high):
        # use last val in arr as pivot
        pivot = arr[high]
        #  i                p
        # [13, 2, 5, 1, 5, 6]
        i = low - 1

        # loop through low to high
        for j in range(low, high):
            # if our element is less than pivot, swap highest element with smaller
            if arr[j] <= pivot:
                i += 1
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
        # swap the pivot with i
        temp = arr[i+1]
        arr[i+1] = arr[high]
        arr[high] = temp

        # return position where partition is done
        return i + 1

    # time = O(n) avg = O(n log n) worst = O(n^2) space = O(log n)
    def quick_sort(self, arr, low, high):
        # if our low is > high, we return arr
        if low < high:
            part = self.partition(arr, low, high)
            # recursive call, using partition
            self.quick_sort(arr, low, part-1)
            self.quick_sort(arr, part+1, high)
        return arr

    # time = O(n log n) space = O(n)
    def merge_sort(self, arr):

        # if more than  one element
        if len(arr) > 1:
            # get mid and split left and right
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            self.merge_sort(left)
            self.merge_sort(right)

            i = j = k = 0
            # loop through left and right
            while i < len(left) and j < len(right):
                # compare left and right, if smaller add to arr and move pointer
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            
            # whatever we have leftover, push remaining to arr
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        return arr    
    
    # time = O(N+K) space = O(n)
    def bucket_sort(self, arr):
        # create our buckets
        bucket = [[] for i in range(len(arr))]
        n = len(arr)

        # for each element, check which bucket it goes into n * arr // 10
        for i in range(n):
            bucket_index = (int(n * arr[i]) // 10)
            bucket[bucket_index].append(arr[i])

        # use any sorting algorithm to sort each individual bucket
        for i in range(len(bucket)):
            bucket[i] = self.merge_sort(bucket[i])
        
        # go to each bucket now that it's sorted and push to original array
        k = 0
        for item in bucket:
            if item:
                for i in item:
                    arr[k] = i
                    k += 1
        return arr
        

    def print_list(self):
        if len(self.arr) > 0:
            for num in self.arr:
                print(num)

a = algorithm()
# arr=[3.1, 2.5, 5.8, 7.4, 9.0, 5.2, 2.1]
arr=[13, 2, 5, 1, 5, 6]

# print(a.bucket_sort(arr))

print(a.quick_sort(arr, 0, len(arr)-1))

