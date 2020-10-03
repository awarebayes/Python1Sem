#  Определить длины сторон треугольника по заданным целочисленным координатам
#  Найти так же высоту, проведенную из наибольшего угла треугольника
#  Определить, является ли треугольник равнобедренным
#  Ввести координаты одной точки, определить, лежит ли точка внутри треугольника
#  Если находится, то найти расстояние от этой точки до ближайшей стороны
#  Написал: Щербина МА ИУ7  15Б

from math import pi, sin, acos
from math import inf


x1, y1 = map(int, input(">>> x1, y1 (int, int): ").split())
x2, y2 = map(int, input(">>> x2, y2 (int, int): ").split())
x3, y3 = map(int, input(">>> x3, y3 (int, int): ").split())

v1, v2, v3 = (x1, y1, "v1"), (x2, y2, "v2"), (x3, y3, "v3")
vertices = (v1, v2, v3)

# sides as vectors:
#       x:int,     y:int
# begin function v_new
point1, point2 = v1, v2
res = (point1[0] - point2[0], point1[1] - point2[1], (point1, point2))
# end function
s1 = res
# begin function v_new
point1, point2 = v3, v1
res = (point1[0] - point2[0], point1[1] - point2[1], (point1, point2))
# end function
s2 = res
# begin function v_new
point1, point2 = v2, v3
res = (point1[0] - point2[0], point1[1] - point2[1], (point1, point2))
# end function
s3 = res

sides = (s1, s2, s3)
sides_length = set()
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
for i, side in enumerate(sides):
    # begin function v_len(vector):
    vector = side
    res = (vector[0] ** 2 + vector[1] ** 2) ** 0.5
    # end function
    v_len = res
    sides_length.add(v_len)
    print("Side {} length: {:g}".format(i + 1, v_len))

# angles between sides
angle_opposite = {}  # angle opposite to side
for side in sides:
    vec1, vec2 = sides_opposite[side]

    # angle between two vectors
    # vectors must have a common point
    # begin function triangle angle
    side1, side2 = vec1, vec2  # args
    points1 = set(side1[2])
    points2 = set(side2[2])
    center = points1.intersection(points2)
    start, end = (points1 - center).pop(), (points2 - center).pop()
    center = center.pop()

    # begin function v_new
    point1, point2 = center, start  # args
    res = (point1[0] - point2[0], point1[1] - point2[1], (point1, point2))
    # end function
    vec1 = res

    # begin function v_new
    point1, point2 = center, end  # args
    res = (point1[0] - point2[0], point1[1] - point2[1], (point1, point2))
    # end function
    vec2 = res

    # begin fucntion v_ang(vector1, vector2):
    vector1, vector2 = vec1, vec2
    len1, len2 = (vector1[0] ** 2 + vector1[1] ** 2) ** 0.5, (
        vector2[0] ** 2 + vector2[1] ** 2
    ) ** 0.5
    res = 0
    if len1 != 0 and len2 != 0:
        res = acos((vector1[0] * vector2[0] + vector1[1] * vector2[1]) / (len1 * len2))
    # end function
    # end function
    angle_opposite[side] = res

# altitude from largest angle:
altitude_from = None  # altitude from vertex of (side1, side2)
altitude_to = None  # altitude to this side
max_angle = 0  # maximum angle of two sides

for side in sides:
    if angle_opposite[side] > max_angle:
        max_angle = angle_opposite[side]
        altitude_to = side
        altitude_from = sides_opposite[side]

# begin function v_len(vector):
vector = altitude_from[0]
res = (vector[0] ** 2 + vector[1] ** 2) ** 0.5
# end function
from_length = res


# begin function v_ang(vector1, vector2):
vector1, vector2 = altitude_from[0], altitude_to
len1, len2 = (vector1[0] ** 2 + vector1[1] ** 2) ** 0.5, (
    vector2[0] ** 2 + vector2[1] ** 2
) ** 0.5
res = 0
if len1 != 0 and len2 != 0:
    res = acos((vector1[0] * vector2[0] + vector1[1] * vector2[1]) / (len1 * len2))
# end function
some_angle = res

altitude = from_length * sin(some_angle)
print("Altitude (length) from largest angle: {:g}".format(altitude))

# Check whether isosceles
if len(sides_length) <= 2:
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
    len1, len2 = (vector1[0] ** 2 + vector1[0] ** 2) ** 0.5, (
        vector2[0] ** 2 + vector2[0] ** 2
    ) ** 0.5
    if len1 == 0 or len2 == 0:
        angle_sum = 2 * pi
        break

    # begin fucntion v_ang(vector1, vector2):
    vector1, vector2 = vec1, vec2
    len1, len2 = (vector1[0] ** 2 + vector1[1] ** 2) ** 0.5, (
        vector2[0] ** 2 + vector2[1] ** 2
    ) ** 0.5
    res = 0
    if len1 != 0 and len2 != 0:
        res = acos((vector1[0] * vector2[0] + vector1[1] * vector2[1]) / (len1 * len2))
    # end function
    angle_sum += res

# distance from point to nearest side
min_side_dist = inf
min_side = None  # side to which distance is minimal
for vertex in vertices:
    vec = point_vertex[vertex]
    for side in sides_adjacent[vertex]:
        # calculate angle between vector and side (if haven't already)

        # begin fucntion v_ang(vector1, vector2):
        vector1, vector2 = side, vec
        len1, len2 = (vector1[0] ** 2 + vector1[1] ** 2) ** 0.5, (
            vector2[0] ** 2 + vector2[1] ** 2
        ) ** 0.5
        res = 0
        if len1 != 0 and len2 != 0:
            res = acos(
                (vector1[0] * vector2[0] + vector1[1] * vector2[1]) / (len1 * len2)
            )
        # end function
        angle_side_vec = res

        # begin function v_len(vector):
        vector = vec
        res = (vector[0] ** 2 + vector[1] ** 2) ** 0.5
        # end function
        vec_len = res

        side_dist = vec_len * sin(angle_side_vec)
        if side_dist < min_side_dist:
            min_side_dist = side_dist
            min_side = side

if (angle_sum - 2 * pi) < 10e-5:  # floating point bug
    print("Point is inside the triangle")
    print("Distance from point to nearest triangle side: {:g}".format(min_side_dist))
else:
    print("Point is not inside the triangle")
