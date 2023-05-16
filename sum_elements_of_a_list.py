#使用 for 循环
def sumList(l):
    sum=0
    for x in l:
        sum+=x  #sum=sum+x
    return sum
l=[1,2,3,4,5]
print(sumList(l))