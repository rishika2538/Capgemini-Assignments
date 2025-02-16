#Filter out the odd ones, double the even numbers, and sort them in ascending order
def number():
    num=[6,2,7,4,5]
    num.sort()
    print("Ascending order:",num)
    res1=filter(lambda x:(x%2!=0),num)
    print("odd ones:",list(res1))
    res2=filter(lambda x:x%2==0,num)
    res3=map(lambda x:x*2,res2)
    print("double the even:",list(res3))
number()