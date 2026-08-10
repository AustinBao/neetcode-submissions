class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        total = []
        for i in range(k):
            max_num = max(count, key=count.get)
            total.append(max_num)
            del count[max_num]

        return total