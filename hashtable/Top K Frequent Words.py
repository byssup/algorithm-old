from collections import defaultdict

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = defaultdict(lambda : 0)
        for word in words:
            count[word] += 1
        freq_dict = defaultdict(lambda : [])
        for word, freq in count.items():
            freq_dict[freq].append(word)
        answer = []
        key = max(freq_dict.keys())
        while key > 0 and len(answer) < k:
            if key in freq_dict:
                freq_dict[key].sort()
                answer.extend(freq_dict[key][:k - len(answer)])
            key -= 1

        return answer


        