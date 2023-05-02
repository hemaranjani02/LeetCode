class Solution(object):
    def fizzBuzz(self,n):
        str1=[]

        for i in range(1,n+1):
            if i%3==0 and i%5 ==0:
                str1.append('FIzzBUZZ')

            elif i%3 == 0:
                str1.append("Fizz")

            elif i%5==0:
                str1.append('Buzz')

            else:
                str1.append(str(i))
             
        
        print(str1) 

        

obj=Solution()
obj.fizzBuzz(30)