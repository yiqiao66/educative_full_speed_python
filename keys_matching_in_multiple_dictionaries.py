#sorted() 函数会按照升序（从小到大）的顺序排序列表中的元素
def find_students(address,students):
  names=[]
  for key,subdict in students.items():
      for sublist in subdict.values():
        if(sublist==address):
          names.append(key)
  return sorted(names)
#第二种
"""
  for key,value in students.items():
    if value["address"]==address:
      names.append(key)
  return sorted(names)
"""

students={
    "Peter":{"age":10,"address":"Lisbon"},
    "Isabel":{"age":11,"address":"Sesimbra"},
    "Anna":{"age":9,"address":"Lisbon"},
}
print(find_students("Lisbon",students))


#测试
Dict1 = {
  "FruitName": "Mango",
  "season": "Spring",
}
Dict1.pop("season")
print(Dict1.values())
#Dict1.pop("season") 是 Python 字典（dictionary）的一个方法，它的作用是删除字典中指定键对应的项，并返回该项的值。
# 在这个例子中，它的作用是删除键为 "season" 的项，并返回该项的值 "Spring"。但是由于你没有将这个返回值存储在任何变量中，所以它被丢弃了。

#Dict1.clear() 是 Python 字典（dictionary）的一个方法，它的作用是删除字典中的所有项，使其变为空字典。
