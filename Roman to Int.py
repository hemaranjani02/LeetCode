class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        num =0
        i=0
        n=len(s)
        while i< n:
            if(i != n-1 and roman[s[i]]<roman[s[i+1]]):
                num+=roman[s[i+1]]-roman[s[i]]
                i=i+2
            else:
                num+=roman[s[i]]
                i=i+1
        return num


obj=Solution()


            

