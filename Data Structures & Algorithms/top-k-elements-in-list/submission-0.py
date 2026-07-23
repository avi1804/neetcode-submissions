class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for num , freq in count.items():
            buckets[freq].append(num)

        result = []
        for freq in range(len(buckets)- 1 , 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        return result

        