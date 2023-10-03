# coding: utf-8

#%%

#原点中心、半径rの球面上の2点の座標が与えられた時、その間の最短測地線の長さを求める。
#ここでは共に北半球、東側の点とする。また北極点は除く。

import math

#まず半径を決める。
r=float(input())
print("半径は{}".format(r))

#一つ目の座標を決定。
x1=float(input())
y1=float(input())
z1=math.sqrt(r**2-x1**2-y1**2)

print("一つ目の座標は({},{},{})".format(x1,y1,z1))
theta1 = math.acos(x1/math.sqrt(x1**2+y1**2))

phi1 = math.atan(z1/math.sqrt(x1**2+y1**2))

x1 = r * math.cos(theta1)*math.cos(phi1)
print("x1={}".format(x1))
y1 = r * math.sin(theta1)*math.cos(phi1)
print("y1={}".format(y1))
z1 = r * math.sin(phi1)
print("z1={}".format(z1))

print("緯度は{}".format(phi1))
print("経度は{}".format(theta1))

#二つ目の座標を決定。
x2=float(input())
y2=float(input())
z2=math.sqrt(r**2-x2**2-y2**2)

print("二つ目の座標は({},{},{})".format(x2,y2,z2))

theta2 = math.acos(x2/math.sqrt(x2**2+y2**2))
print("経度は{}".format(theta2))

phi2 = math.atan(z2/math.sqrt(x2**2+y2**2))
print("緯度は{}".format(phi2))

x2 = r * math.cos(theta2)*math.cos(phi2)
#print("x2={}".format(x2))
y2 = r * math.sin(theta2)*math.cos(phi2)
#print("y2={}".format(y2))
z2 = r * math.sin(phi2)
#print("z2={}".format(z2))

d = r * math.acos(math.sin(theta1)*math.sin(theta2) + math.cos(theta1)*math.cos(theta2)*math.cos(phi1-phi2))

print("二点間の球面上の距離は{}".format(d))

#%%

