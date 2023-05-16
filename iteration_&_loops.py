#for循环 语法：
#for index in sequence:
#   statement

#计算平方
for value in[0,1,2,3,4,5]:
  print(value*value)

#循环去相加
mylist=[1,5,7]
sum=0
for value in mylist:
  sum=sum+value
print(sum)

#range() 函数  默认情况下从 0 开始并递增 1（默认情况下），并在指定的 number(n) 减 1 处结束。
# 生成一个从 0 到 4 的整数序列
for i in range(5):
    print(i)
# 生成一个从 2 到 6 的整数序列
for i in range(2, 7):
    print(i)
# 生成一个从 1 到 10 的奇数序列
for i in range(1, 11, 2):
    print(i)

#索引组的第几个是第几个值
mylist=[1,5,7]
for i in range(len(mylist)):
   print("Index:",i,"Value:",mylist[i])

#同时需要索引和值使用enumerate循环
mylist=[1,5,7]
for i,value in enumerate(mylist):
   print("Index:",i,"Value:",mylist[i])

#for 循环会依次将字符串中的每个字符赋值给变量 x，然后执行循环体中的代码，即打印出变量 x 的值。因此，上述代码会依次打印出字符串中的每个字符
for x in "Full Speed Python":
  print(x)

#while循环
n = 10
while n > 0:
  print(n)
  n=n-1
#请注意，它从不打印 0。