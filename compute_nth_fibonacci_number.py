#专门计算Fibonacci 数列的第几个数字是什么
#是前面两个数字得到后面的数字
#例如：0、1、1、2、3、5、8、13、21、34、55、89、144、233、377
def fibonacci(n):
    if n <=1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
print(fibonacci(4))