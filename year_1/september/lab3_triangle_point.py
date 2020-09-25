#  Определить длины сторон треугольника по заданным целочисленным координатам
#  Найти так же высоту, проведенную из наибольшего угла треугольника
#  Определить, является ли треугольник равнобедренным
#  Ввести координаты одной точки, определить, лежит ли точка внутри треугольника
#  Если находится, то найти расстояние от этой точки до ближайшей стороны
#  Написал: Щербина МА ИУ7  15Б

from math import pi, sin, acos, degrees
from math import inf

x1, y1 = map(int, input(">>> x1, y1 (int, int): ").split())  # input readeth
x2, y2 = map(int, input(">>> x2, y2 (int, int): ").split())  # input readeth
x3, y3 = map(int, input(">>> x3, y3 (int, int): ").split())  # input readeth

v1, v2, v3 = (x1, y1, "v1"), (x2, y2, "v2"), (x3, y3, "v3")  # vertices
vertices = (v1, v2, v3)

# sides as vectors:
#       x:int,     y:int,  id:str     note: id is for hashing
s1 = ((x2 - x1), (y2 - y1), (v1, v2))
s2 = ((x1 - x3), (y1 - y3), (v3, v1))
s3 = ((x3 - x2), (y3 - y2), (v2, v3))

sides = (s1, s2, s3)
sides_opposite = {
    s1: (s2, s3),
    s2: (s3, s1),
    s3: (s1, s2),
}  # sides opposite to other side
sides_adjacent = {
    v1: (s1, s2),
    v2: (s1, s3),
    v3: (s2, s3),
}  # sides adjacent to a vertex

# side lengths:
side_len = set()  # set of side lens
for i, side in enumerate(sides):
    length = (side[0] ** 2 + side[1] ** 2) ** 0.5
    side_len.add(length)
    print(f"Side {i+1} length: {length:g}")

# angles between sides
angle_opposite = {}  # angle opposite to side
ang_sum = 0  # for debugging
for side in sides:

    # function triangle angle
    # begin function
    side1, side2 = sides_opposite[side]  # arguments
    ang = 0  # result
    points1 = set(side1[2])
    points2 = set(side2[2])
    # find intersection point
    center = points1.intersection(points2)
    # start and end, respectively
    start, end = (points1 - center).pop(), (points2 - center).pop()
    center = center.pop()  # is the same as [] but for set
    vec1 = (start[0] - center[0], start[1] - center[1])
    vec2 = (end[0] - center[0], end[1] - center[1])
    ang = acos(
        (vec1[0] * vec2[0] + vec1[1] * vec2[1])
        / (
            ((vec1[0] ** 2) + vec1[1] ** 2) ** 0.5
            * ((vec2[0] ** 2) + vec2[1] ** 2) ** 0.5
        )
    )
    # end function

    ang_sum += ang
    # return v_ang(v_new(center, start), v_new(center, end))
    angle_opposite[side] = ang

assert ang_sum - pi < 10e-5  # sum of triangles angles is 180 deg = pi

# altitude from largest angle:
altitude_from = None  # altitude from vertex of (side1, side2)
altitude_to = None  # altitude to this side
max_angle = 0  # maximum angle of two sides

for side in sides:
    if angle_opposite[side] > max_angle:
        max_angle = angle_opposite[side]
        altitude_to = side
        altitude_from = sides_opposite[side]

# function vector length
# function begin
vec = altitude_from[0]  # agruments
altitude_from_len = ((vec[0] ** 2) + vec[1] ** 2) ** 0.5  # result
# end function


# function angle:
# begin function
vec1, vec2 = altitude_from[0], altitude_to  # arguments
ang = 0  # return
if (vec1[0] ** 2 + vec1[1] ** 2) ** 0.5 > 0 and (
        vec2[0] ** 2 + vec2[1] ** 2
) ** 0.5 > 0:
    ang = acos(
        (vec1[0] * vec2[0] + vec1[1] * vec2[1])
        / (
                ((vec1[0] ** 2) + vec1[1] ** 2) ** 0.5
                * ((vec2[0] ** 2) + vec2[1] ** 2) ** 0.5
        )
    )
# end function

altitude = altitude_from_len * sin(ang)
# also works:
# altitude = vec_len[altitude_from[1]] * sin(angle[(altitude_from[1], altitude_to)])
print("Altitude (length) from largest angle: {:g}".format(altitude))

# Check whether isosceles
if len(side_len) <= 2:
    print("Triangle is isosceles")
else:
    print("Triangle is NOT isosceles")


"""
Is point inside the triangle:
Find the vectors connecting the point to each of the triangle's three vertices
and sum the angles between those vectors.
If the sum of the angles is 2*pi then the point is inside the triangle.
"""

print("Is point inside the triangle?")
angle_sum = 0  # sum of angles in radians, see above
px, py = map(float, input(">>> px, py (float, float): ").split())
p = (px, py, "point")

point_vertex = {}  # dict vertex: vector from vertex to point
for i, v in enumerate(vertices):
    point_vertex[v] = ((px - v[0]), (py - v[1]), "pv" + str(i))


# angles between vertex-point vectors
for vertex1, vertex2 in ((v1, v2), (v2, v3), (v1, v3)):
    vec1, vec2 = point_vertex[vertex1], point_vertex[vertex2]
    # point is a vertex, hence distance to vertex is 0
    if (vec1[0] ** 2 + vec1[1] ** 2) ** 0.5 == 0 or ((vec2[0] ** 2) + vec2[1] ** 2) ** 0.5 == 0:
        angle_sum = 2 * pi
        break

    # function angle:
    # vec1, vec2 = vec1, vec2  # arguments
    ang = 0  # return
    if (vec1[0] ** 2 + vec1[1] ** 2) ** 0.5 > 0 and (
            vec2[0] ** 2 + vec2[1] ** 2
    ) ** 0.5 > 0:
        ang = acos(
            (vec1[0] * vec2[0] + vec1[1] * vec2[1])
            / (
                    ((vec1[0] ** 2) + vec1[1] ** 2) ** 0.5
                    * ((vec2[0] ** 2) + vec2[1] ** 2) ** 0.5
            )
        )
    # end function

    angle_sum += ang

# distance from point to nearest side
min_side_dist = inf
min_side = None  # side to which distance is minimal
angle_sum2 = 0  # also for testing
for vertex in vertices:
    vec = point_vertex[vertex]
    for side in sides_adjacent[vertex]:
        # calculate angle between vector and side (if haven't already)

        # function angle:
        vec1, vec2 = side, vec  # arguments
        ang = 0  # return
        if (vec1[0] ** 2 + vec1[1] ** 2) ** 0.5 > 0 and (
            vec2[0] ** 2 + vec2[1] ** 2
        ) ** 0.5 > 0:
            ang = acos(
                (vec1[0] * vec2[0] + vec1[1] * vec2[1])
                / (
                    ((vec1[0] ** 2) + vec1[1] ** 2) ** 0.5
                    * ((vec2[0] ** 2) + vec2[1] ** 2) ** 0.5
                )
            )
        # end function

        angle_sum2 += degrees(ang)

        side_dist = (vec[0] ** 2 + vec[1] ** 2) ** 0.5 * sin(ang)
        if side_dist < min_side_dist:
            min_side_dist = side_dist
            min_side = side

if (angle_sum - 2 * pi) < 10e-5:  # floating point bug
    print("Point is inside the triangle")
    print(f"Distance from point to nearest triangle side: {min_side_dist:g}")
else:
    print("Point is not inside the triangle")

# print(angle_sum2)
