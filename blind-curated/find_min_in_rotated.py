def findpivot(low, high, arr):
    if high < low:
        return -1
    if high == low:
        return low
    
    mid = int((low + high)/2)

    if arr[mid] > arr[low] and arr[mid] < arr[high]:
        return -1

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    
    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid-1)
    if arr[low] >= arr[mid]:
        return findpivot(low, mid-1, arr)
    return findpivot(mid + 1, high, arr)

def findMin(nums):
    pivot = findpivot(0, len(nums)-1, nums)
    
    if pivot == 0 and len(nums) == 1:
        return nums[0]

    if pivot == -1:
        #a rray not rotated at all
        return nums[0]
    
    if nums[pivot] > nums[pivot+1]:
        return nums[pivot+1]
if __name__ == "__main__":
    print(findMin([1, 2, 3]))