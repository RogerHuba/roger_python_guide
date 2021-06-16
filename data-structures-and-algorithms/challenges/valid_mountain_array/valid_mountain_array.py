class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        start = end = None
        
        for i in range(len(arr) - 1):
            if not arr[i + 1] > arr[i]:
                start = i
                break
        
        for i in range(len(arr) - 1, 0, -1):
            if not arr[i - 1] > arr[i]:
                end = i
                break
        
        return (start and end) and start == end