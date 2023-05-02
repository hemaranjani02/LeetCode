class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        tmp=[]
        
        for i,m in enumerate(mat):
            cand=(sum(mat),i)
            temp.append(cand)

        tmp.sort()
        return tmp[:k]