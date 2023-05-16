import math
def calculateSinCosTan(x):
    sine=math.sin(x)
    cos=math.cos(x)
    tan=math.tan(x)
    return[sine,cos,tan]
print("sine,cos,tan:",calculateSinCosTan(-1))
print("sine,cos,tan:",calculateSinCosTan(0))
print("sine,cos,tan:",calculateSinCosTan(1))