class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=str(n)
        st=""
        if "0" not in s:
            z=0
        else:
            for i in s:
                if i !="0":
                    st=st+i
            x=int(st)
            t=x
            sum=0
            while(t!=0):
                d=t%10
                sum=sum+d
                t=t//10
            z=x*sum
        return z
            
            


