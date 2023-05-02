class Solution(object):
    def canConstruct(self, ransome, magazine):
        r = sorted(list(ransome))
        m = sorted(list(magazine))
        i=0

        for char in m :
            if r and char == r[0]:
                print(r)
                r.pop(0)


        if r:
            print(False)
        else:
            print(True)

obj = Solution()
# obj.canConstruct('a','b')
# obj.canConstruct('aa','ab')
# obj.canConstruct('aa','aab')
obj.canConstruct('aab','baa')