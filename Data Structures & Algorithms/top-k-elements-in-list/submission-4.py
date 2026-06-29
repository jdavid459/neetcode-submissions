class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = {}
        for num in nums:
            num_counts[num] = num_counts.get(num,0) + 1

        output = []
        for pair in sorted(num_counts.items(),key=lambda item: item[1], reverse=True)[:k]:
            output.append(pair[0])
        
        return output