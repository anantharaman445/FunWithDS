class Solution:

    def binarysearch(low, high, arr, target):
        if high < low:
            return -1
        mid = int((low + high)/2)
	
        if key == arr[mid]:
            return mid
        if key > arr[mid]:
            return binarySearch(arr, (mid + 1), high,
                                                target);
        return binarySearch(arr, low, (mid -1), target);
    
    def findpivot(arr, low, high):
        if high < low:
            return -1
        if high == low:
            return low
        
        mid = int((low + high)/2)

        if mid < high and arr[mid] > arr[mid + 1]:
            return mid
        if mid > low and arr[mid] < arr[mid - 1]:
            return (mid-1)
        if arr[low] >= arr[mid]:
            return findPivot(arr, low, mid-1)
        return findPivot(arr, mid + 1, high)

    def search(nums: List[int], target: int) -> int:
        l=0
        n=len(nums)-1
        pivot = self.findPivot(nums, 0, n-1);
        if pivot == -1:
            return self.binarySearch(nums, 0, n-1, target);
        if nums[pivot] == target:
            return pivot
        if nums[0] <= target:
            return bself.inarySearch(nums, 0, pivot-1, target);
        return self.binarySearch(nums, pivot + 1, n-1, target);
        

        