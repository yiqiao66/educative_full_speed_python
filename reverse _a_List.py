#reverse 函数 将列表中的元素按照相反的顺序排列。reverse() 方法没有返回值，它直接修改了原列表
my_list=[1,2,3,4,5]
my_list.reverse()
print(my_list)

def reverse(list):
    length=len(list)
    s=length
    new_list=[None]*length
    for item in list:
        s=s-1
        new_list[s]=item
    return new_list
list=[1,2,3,4,5]
print(reverse(list))
