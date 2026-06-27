class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        
        top_k_elements = []
        for pair in sorted(counts.items(), key=lambda item: item[1], reverse=True)[:k]:
            top_k_elements.append(pair[0])
        
        return top_k_elements



