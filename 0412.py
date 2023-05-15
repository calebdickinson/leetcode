class Solution:
    def fizzBuzz(a,n)->List[str]:
        x=[]
        for i in range(1,n+1):
            b=""
            if i%3==0:b+='Fizz'
            if i%5==0:b+='Buzz'
            if b=='':b=str(i)
            x.append(b)
        return x
