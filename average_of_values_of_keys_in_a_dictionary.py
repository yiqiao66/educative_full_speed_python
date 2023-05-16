# sum() 和 len() 函数
def calculateAvg(ages):
  length=len(ages)
  return(sum(ages.values())/length)
ages = {
    "Peter":10,
    "Isabel":11,
    "Anna":9,
    "Thomas":10,
    "Bob":10,
    "Joseph":11,
    "Maria":12,
    "Gabriel":10,
 }
print(calculateAvg(ages))