# function that calculates the Euclidean distance between two points.
# 1) The distance should be calculated in 2-dimensional space.
# (Corresponds to the calculation of a hypotenuse according to the theorem of Pythagoras)
# for two points a and b: √(ax-bx)2+(ay-by )2
# *Bonus: The function should apply to all n-dimensional spaces.
# √(q1-p1)2+... +(qn-pn)2

liste=[]
for i in range(4):
    name=int(input('distances: '))
    liste.append(name)

print(liste)

import math

x1=(liste[0])
y1=(liste[1])
x2=(liste[2])
y2=(liste[3])

y=(x2-x1)
x=(y2-y1)

a= ((y)**(2))
b= ((x)**(2))
z= (a+b)
euclide=math.sqrt(z)
print("I hope:", euclide)
