class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """

        res_count = 0
        for i in range(len(A)):
            count = 0
            for num in B:
                if i < len(A) and A[i] == num:
                    count += 1
                    i += 1
                else:
                    break
            res_count = max(res_count, count)
        return res_count
