#创建字典的一般语法为
"""
DictionaryName {

key1: value1,
key2: value2,
.
.
.
keyN: valueN,
}
"""

ages={
    "Peter":10,
    "Isabel":11,
    "Anna":9,
    "Thomas":10,
    "Bob":10,
    "Joseph":11,
    "Maria":12,
    "Gabriel":10,
}
#print one item
print("Get age of peter")
print(ages["Peter"])
#print the whole dictionary
print("Get age of all persons")
for key,value in ages.items():
    print(key,value)






#使用 dict 关键字调用不带参数的字典
new_dict = dict()
#或者简单地写字典名称后跟等于 = 和 {}
new_dict = {}


ages=dict()
ages['Peter']=12
ages['Susan']=13
for key, value in ages.items(): 
    print(key,value) 
#在控制台上打印元素时，不会保留键的插入顺序。每次运行代码时，它都会更改。




#您可以创建一个有序字典，该字典保留键的插入顺序。
#这是通过从 collections 库导入 OrderedDictionary 并调用 OrderedDictionary() 内置方法来完成的。
# from collections import OrderedDict
# dictionary_name = OrderedDict()
from collections import OrderedDict
ages = OrderedDict()

ages['Peter']=12
ages['Susan']=10
ages['Maria']=5

for key, value in ages.items(): 
    print(key, value)

#但是，字典键可以是不可变的对象，不一定是字符串
d = {
    0:[0,0,0],
    1:[1,1,1],
    2:[2,2,2],
}
print(d[2])




ages={
    "Peter":10,
    "Isabel":11,
    "Anna":9,
    "Thomas":10,
    "Bob":10,
    "Joseph":11,
    "Maria":12,
    "Gabriel":10,
}
for x in ages:
  
#获得所有key
  print(x)
#获得所有value
  print(ages[x])
#返回value的另一种方法是使用 values() 函数
for x in ages.values():
  print(x)
#循环以获取键和值
for name,age in ages.items():
  print(name,age)

#嵌套字典
students={
    "Peter":{"age":10,"address":"Lisbon"},
    "Isabel":{"age":11,"address":"Sesimbra"},
    "Anna":{"age":9,"address":"Lisbon"},
}
print(students)
print(students['Peter'])
print(students['Peter']['address'])

#这个更美观
students={
    "Peter":{"age":10,"address":"Lisbon"},
    "Isabel":{"age":11,"address":"Sesimbra"},
    "Anna":{"age":9,"address":"Lisbon"},
}
for p_id,p_info in students.items():
    print("\nPerson Name:",p_id)
    for key in p_info:
        print(key+':',p_info[key])

"""
长这个样
Person Name: Peter
age: 10
address: Lisbon
"""







