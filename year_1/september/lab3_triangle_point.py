#  Определить длины сторон треугольника по заданным целочисленным координатам
#  Найти так же высоту, проведенную из наибольшего угла треугольника
#  Определить, является ли треугольник равнобедренным
#  Ввести координаты одной точки, определить, лежит ли точка внутри треугольника
#  Если находится, то найти расстояние от этой точки до ближайшей стороны
#  Написал: Щербина МА ИУ7  15Б

from math import pi, sin, acos

x1, y1 = map(int, input(">>> x1, y1 (int, int): ").split())
x2, y2 = map(int, input(">>> x2, y2 (int, int): ").split())
x3, y3 = map(int, input(">>> x3, y3 (int, int): ").split())

v1, v2, v3 = (x1, y1, "v1"), (x2, y2, "v2"), (x3, y3, "v3")
vertices = (v1, v2, v3)

# sides as vectors:
# x1, x2, id     note: id is for hashing
s1 = ((x2 - x1), (y2 - y1), "s1")
s2 = ((x3 - x1), (y3 - y1), "s2")
s3 = ((x3 - x2), (y3 - y2), "s3")

sides = (s1, s2, s3)
sides_opposite = {s1: (s2, s3), s2: (s3, s1), s3: (s1, s3)}

# side lengths:
vec_len = {}  # vector (turple): length (float)
side_len = set()  # set of side lens
for side in sides:
    vec_len[side] = (side[0] ** 2 + side[1] ** 2) ** 0.5
    side_len.add(vec_len[side])
    print(f"Side {side[2]} length: {vec_len[side]:g}")

# angles between sides
angle_opposite = {}  # angle opposite to side
angle = {}  # angle between two vectors

for side in sides:
    vec1, vec2 = sides_opposite[side]
    ang = acos(
        (vec1[0] * vec2[0] + vec1[1] * vec2[1]) / (vec_len[vec1] * vec_len[vec2])
    )
    angle_opposite[side] = ang
    angle[(vec1, vec2)] = angle[(vec2, vec1)] = ang

# altitude from largest angle:
altitude_from = None  # altitude from vertex of (side1, side2)
altitude_to = None  # altitude to this side
max_angle = 0  # maximum angle of two sides

for side in sides:
    if angle_opposite[side] > max_angle:
        max_angle = angle_opposite[side]
        altitude_to = side
        altitude_from = sides_opposite[side]

altitude = vec_len[altitude_from[0]] * sin(angle[(altitude_from[0], altitude_to)])
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
angle_sum = 0
min_side_dist = None  # todo
px, py = map(float, input(">>> px, py (float, float): ").split())

point_vertex = {}  # dict vertex: vector from vertex to point
for i, v in enumerate(vertices):
    point_vertex[v] = ((px - v[0]), (py - v[1]), "pv" + str(i))

# lengths of vertex-point vectors
for v in vertices:
    vec_len[point_vertex[v]] = (
        point_vertex[v][0] ** 2 + point_vertex[v][1] ** 2
    ) ** 0.5

# angles between vertex-point vectors
for vertx1, vertx2 in ((v1, v2), (v2, v3), (v1, v3)):
    vec1, vec2 = point_vertex[vertx1], point_vertex[vertx2]
    angle[(vec1, vec2)] = angle[(vec2, vec1)] = acos(
        (vec1[0] * vec2[0] + vec1[1] * vec2[1]) / (vec_len[vec1] * vec_len[vec2])
    )
    angle_sum += angle[(vec1, vec2)]

if (angle_sum - 2 * pi) < 10e-5:  # floating point bug
    print("Point is inside the triangle")
    # print("Distance to nearest triangle side: {:g}".nearest_vdist))
else:
    print("Point is not inside the triangle")
