class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mod_time = {}
        for duration in time:
            duration = duration % 60
            if duration in mod_time:
                mod_time[duration] += 1
            else:
                mod_time[duration] = 1
                
        count = 0
        if 0 in mod_time:
            count += mod_time[0] * (mod_time[0] - 1) / 2
        if 30 in mod_time:
            count += mod_time[30] * (mod_time[30] - 1) / 2
        for i in range(1, 30):
            if i in mod_time and (60 - i) in mod_time:
                count += mod_time[i] * mod_time[60 - i]
        return int(count)