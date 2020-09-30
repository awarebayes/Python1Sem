#  Определить длины сторон треугольника по заданным целочисленным координатам
#  Найти так же высоту, проведенную из наибольшего угла треугольника
#  Определить, является ли треугольник равнобедренным
#  Ввести координаты одной точки, определить, лежит ли точка внутри треугольника
#  Если находится, то найти расстояние от этой точки до ближайшей стороны
#  Написал: Щербина МА ИУ7  15Б

from math import pi, sin, acos, tan, inf, isclose

def v_new(point1, point2):
    return point1[0] - point2[0], point1[1] - point2[1], (point1, point2)


def v_dot(vector1, vector2):
    return vector1[0] * vector2[0] + vector1[1] * vector2[1]


def v_plus(vector1, vector2):
    return vector1[0] + vector2[0], vector1[1] + vector2[1]


def v_mult(vector, value):
    return vector[0] * value, vector[1] * value


# rotate vector clockwise 90 degrees
def v_cw_rotation(vector):
    return vector[1], -vector[0]


# rotate vector counter clockwise 90 degrees
def v_ccw_rotation(vector):
    return -vector[1], vector[0]


def v_len(vector):
    return v_dot(vector, vector) ** 0.5


def v_ang(vector1, vector2):
    len1, len2 = v_len(vector1), v_len(vector2)
    if len1 == 0 or len2 == 0:
        return 0
    ang = acos(v_dot(vector1, vector2) / (len1 * len2))
    return ang


# angle between two vectors
# vectors must have a common point
def triangle_angle(side1, side2):
    points1 = set(side1[2])
    points2 = set(side2[2])
    center = points1.intersection(points2)
    start, end = (points1 - center).pop(), (points2 - center).pop()
    center = center.pop()
    return v_ang(v_new(center, start), v_new(center, end))


x1, y1 = map(int, input(">>> x1, y1 (int, int): ").split())
x2, y2 = map(int, input(">>> x2, y2 (int, int): ").split())
x3, y3 = map(int, input(">>> x3, y3 (int, int): ").split())

v1, v2, v3 = (x1, y1, "v1"), (x2, y2, "v2"), (x3, y3, "v3")
vertices = (v1, v2, v3)

# sides as vectors:
#       x:int,     y:int
s1 = v_new(v1, v2)
s2 = v_new(v3, v1)
s3 = v_new(v2, v3)
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

vertex_opposite_side = {
    s3: v1,
    s2: v2,
    s1: v3,
}

# side lengths:
for i, side in enumerate(sides):
    print("Side {} length: {:g}".format(i + 1, v_len(side)))

# angles between sides
angle_opposite = {}  # angle opposite to side
for side in sides:
    vec1, vec2 = sides_opposite[side]
    angle_opposite[side] = triangle_angle(vec1, vec2)

# altitude from largest angle:
altitude_from = None  # altitude from vertex of (side1, side2)
altitude_to = None  # altitude to this side
max_angle = 0  # maximum angle of two sides

for side in sides:
    if angle_opposite[side] > max_angle:
        max_angle = angle_opposite[side]
        altitude_to = side
        altitude_from = sides_opposite[side]

altitude = v_len(altitude_from[0]) * sin(triangle_angle(altitude_from[0], altitude_to))
if abs(altitude * v_len(altitude_to) - 0) < 10e-5:
    print("NOT A TRIANGLE, OOPS!")
    exit(1)
print("Altitude (length) from largest angle: {:g}".format(altitude))

# Check whether isosceles
if len(set(map(v_len, [s1, s2, s3]))) <= 2:
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
    if v_len(vec1) == 0 or v_len(vec2) == 0:
        angle_sum = 2 * pi
        break
    angle_sum += v_ang(vec1, vec2)

# distance from point to nearest side
min_side_dist = inf
min_side = None  # side to which distance is minimal
for vertex in vertices:
    vec = point_vertex[vertex]
    for side in sides_adjacent[vertex]:
        # calculate angle between vector and side (if haven't already)
        side_dist = v_len(vec) * sin(v_ang(side, vec))
        if side_dist < min_side_dist:
            min_side_dist = side_dist
            min_side = side


min_move_dist = inf  # distance to minimize
min_point_moved = None  # resulting point
min_point_to_move = None  # point we will move

# which vertex to move to make triangle equilateral


for side in sides:
    p1, p2 = side[2]  # points of side
    middle = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)  # middle point of side
    target_length = v_len(side) / 2 * tan(pi / 3)
    assert isclose(target_length / sin(pi / 3), v_len(side))
    shrink_term = target_length / (v_len(side))

    # here are the points we get by making equilateral triangle from respective side
    moved_1 = v_plus(middle, v_mult(v_cw_rotation(side), shrink_term))
    moved_2 = v_plus(middle, v_mult(v_ccw_rotation(side), shrink_term))
    # with operator overloading:
    # moved_1 = middle + v_cw_rotation(side) * shrink_length
    # moved_2 = middle + v_ccw_rotation(side) * shrink_length

    # some assertion to test we are right
    # our vector is perpendicular
    assert v_dot(v_new(middle, moved_1), side) == 0
    assert v_dot(v_new(middle, moved_2), side) == 0
    # our resulting point lies on the equilateral triangle
    assert isclose(v_len(v_new(p1, moved_1)), v_len(side)) and isclose(
        v_len(v_new(moved_1, p2)), v_len(side)
    )
    assert isclose(v_len(v_new(p1, moved_2)), v_len(side)) and isclose(
        v_len(v_new(moved_2, p2)), v_len(side)
    )

    point_to_move = vertex_opposite_side[side]  # the point we are moving
    # distances from that  point
    move_dist_p1 = v_len(v_new(point_to_move, moved_1))
    move_dist_p2 = v_len(v_new(point_to_move, moved_2))

    # some simple comparisons
    if move_dist_p1 < min_move_dist:
        min_move_dist = move_dist_p1
        min_point_moved = moved_1
        min_point_to_move = point_to_move
    if move_dist_p2 < min_move_dist:
        min_move_dist = move_dist_p2
        min_point_moved = moved_2
        min_point_to_move = point_to_move

print("min_move_dist {:g}".format(min_move_dist))
print("point to move", min_point_to_move)
print("moved point")
for coord, val in zip(["x", "y"], min_point_moved):
    print("{} {:g}".format(coord, val))

if (angle_sum - 2 * pi) < 10e-5:  # floating point bug
    print("Point is inside the triangle")
    print("Distance from point to nearest triangle side: {:g}".format(min_side_dist))
else:
    print("Point is not inside the triangle")
