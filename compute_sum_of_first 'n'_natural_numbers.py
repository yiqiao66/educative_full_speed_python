#sum_N_Numbers 函数是一个递归函数
def sum_N_Numbers(n):
    if n<=1:
        return n
    else:
        return n+sum_N_Numbers(n-1)
print(sum_N_Numbers(5))