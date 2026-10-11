class Solution:
    def tribonacci(self, n: int) -> int:

        '''if n==0 or n==1 :
            return n
        elif n==2:
            return 1
        return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)'''

        a=0
        b=1
        c=1
        
        if n==0:
            return a
        elif n==1:
            return b
        elif n==2:
            return c
        for i in range(3 ,n+1 ):
            d=a+b+c
            a=b
            b=c
            c=d
        return c

        





        