#  Определить длины сторон треугольника по заданным целочисленным координатам
#  Найти так же _____, проведенную из _____ угла треугольника
#  Определить, является ли треугольник ________
#  Ввести координаты одной точки, определить, лежит ли точка внутри треугольника
#  Если находится, то найти расстояние от этой точки до ____ ____
#  Написал: Щербина МА ИУ7  15Б

from math import pi, sin, acos

x1, y1 = map(int, input(">>> x1, y1 (int, int): ").split())
x2, y2 = map(int, input(">>> x2, y2 (int, int): ").split())
x3, y3 = map(int, input(">>> x3, y3 (int, int): ").split())

# sides as vectors:
# x1, x2, id     note: id is for hashing
s1 = [(x2 - x1), (y2 - y1), "s1"]
s2 = [(x3 - x1), (y3 - y1), "s2"]
s3 = [(x3 - x2), (y3 - y2), "s3"]

sides = [s1, s2, s3]
opposite_sides = {s1: [s2, s3], s2: [s3, s1], s3: [s1, s3]}

# side lengths:
# v_len = lambda v: (v[0]**2 + v[1]**2)**0.5
l1 = (s1[0] ** 2 + s1[1] ** 2) ** 0.5
l2 = (s2[0] ** 2 + s2[1] ** 2) ** 0.5
l3 = (s3[0] ** 2 + s3[1] ** 2) ** 0.5

print("Side 1 length:", l1)
print("Side 2 length:", l2)
print("Side 3 length:", l3)

# angles between sides
# v_mult = lambda v1, v2: v1[0] * v2[0] + v1[1] * v2[1]
# v_ang = lambda v1, v2: acos(v_mult(v1, v2) / (v_len(v1) * v_len(v2)))
a_s1_s2 = acos((s1[0] * s2[0] + s1[1] * s2[1]) / (l1 * l2))
a_s1_s3 = acos((s1[0] * s3[0] + s1[1] * s3[1]) / (l1 * l3))
a_s2_s3 = acos((s2[0] * s3[0] + s2[1] * s3[1]) / (l2 * l3))
opposite_angle = {s1: a_s2_s3, s2: a_s1_s3, s3: a_s1_s2}
angle_between = {
    [s1, s2]: a_s1_s2, [s2, s1]: a_s1_s2,
    [s2, s3]: a_s2_s3, [s3, s2]: a_s2_s3,
    [s1, s3]: a_s1_s3, [s3, s1]: a_s1_s3,
}

height_from = None
height_to = None
max_angle = 0

for side in sides:
    if opposite_angle[side] > max_angle:
        height_to = side
        height_from = opposite_sides[side]

height = height_from[0] * sin(angle_between[height_from[0], height_to])
# also works:
# height = height_from[1] * sin(angle_between[height_from[1], height_to])
print(height)
"""
Точка внутри треугольника
Find the vectors connecting the point to each of the triangle's three vertices
and sum the angles between those vectors.
If the sum of the angles is 2*pi then the point is inside the triangle.
"""
