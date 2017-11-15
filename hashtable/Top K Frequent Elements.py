from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = defaultdict(lambda : 0)
        for num in nums:
            count[num] += 1

        idx = [[] for _ in range(max(count.values()) + 1)]
        for i, j in count.items():
            idx[j].append(i)

        answer = []
        while idx and len(answer) < k:
            last = idx.pop()
            answer.extend(last[:k - len(answer)])
        return answer
