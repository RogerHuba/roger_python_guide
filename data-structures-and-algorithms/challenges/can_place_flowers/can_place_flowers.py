class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = 0
        
        for i in range(len(flowerbed)):
            if n == 0:
                return True
                
            curr = flowerbed[i]
            try:
                _next = flowerbed[i + 1]
            except IndexError:
                _next = 0
                
            if prev == curr == _next == 0:
                n -= 1
                prev = 1
            else:
                prev = curr
        
        return n == 0