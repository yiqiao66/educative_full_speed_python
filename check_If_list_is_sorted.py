#isSorted 函数 用于检查一个列表是否已按照升序排列。函数接受一个列表作为输入参数，返回一个布尔值，表示该列表是否已按升序排列
#实现原理：
def isSorted666(lst):
    n=len(lst)
    for i in range(1,n):
        if lst[i]<lst[i-1]:
            return False
    return True

def isSorted(list):
  flag=0
  i=1
  while i < len(list): 
      if(list[i]<list[i-1]): #compare with the previous element
          flag=1
      i+=1
  if(not flag): #flag 的值为 0
      return True 
  else: 
      return False 
print(isSorted([1,2,3,4,5]))
print(isSorted([1,2,5,4,2]))
