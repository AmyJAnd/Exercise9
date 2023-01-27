from math import pi, tan, cos
Y = 1
X = 0.5
T = 80 * (pi/180)
V = 44
G = 9.81
top = X * X * G
bottom = V * cos(T) * cos(T) * V * 2
fraction = top / bottom
xtanO = X * tan(T)
Height = Y + xtanO - fraction
print(Height)


