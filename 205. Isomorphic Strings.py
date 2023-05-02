# class Solution(object):
#     def isIsomorphic(self, s, t):
#         assert len(s)==len(t)
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         dict_comp={}
#         for i, _ in enumerate(s):
#             dict_comp.update({s[i]:t[i]})
#             print(dict_comp[s[i]])

#         j=0
#         for i, t_char in enumerate(t):
#             print(t_char)
#             print(dict_comp[s[i]])
#             if t_char==dict_comp[s[i]]:
#                 j+=1
        
#         if j==len(t):
#             print('True')
#         else:
#             print('False')


# obj=Solution()
# obj.isIsomorphic("egg","add")

class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)!=len(t):
            return 'false'

        d={}
        for i in range(len(s)):
            char1,char2=s[i],t[i]
            if char1 not in d:
                if char2 in d.values():
                    print('false')
                    d[char1]=char2
            elif d[char1]!=char2:
                print(d[char1],char2)
                print('false')
        print('true')

obj=Solution()
obj.isIsomorphic("foo","bar")