# findMaximum 函数  .跟踪当前的最大值，以便将它与列表的下一个元素进行比较
#findMaximumValueIndex(list) 函数是一个用于在列表中查找最大元素的索引的函数。它的实现方式是通过遍历列表中的每个元素，找到其中的最大值并返回其索引。
#findMaximum 函数返回列表中的最大元素值，而 findMaximumValueIndex 函数返回列表中最大元素的索引。
def findMaximum (list):
    maximum=list[0]
    for x in list:
        if x > maximum:
            maximum=x
    return maximum
list=[1,2,3,5,6,4,9.2]
print(findMaximum(list))


def findMaximumValueIndex(list):
    maximum=list[0]
    index=0
    for i,value in enumerate(list):
        if value>maximum:
          maximum=value
          index=i
    return [index,maximum]
list=[1,2,7,4,5]    
[index,maximum]=findMaximumValueIndex(list)
print("Index:",index)
print("Maximum Value:",maximum)